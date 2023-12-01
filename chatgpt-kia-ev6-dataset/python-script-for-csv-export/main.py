import canedge_browser
import pandas as pd
from datetime import datetime, timezone
import inputs as inp
from utils import (
    setup_fs,
    load_dbc_files,
    restructure_data,
    ProcessData,
    MultiFrameDecoder,
)
import os

tp_type = "uds"
included_bus_channels = [1, 2]
output_file_name = "decoded_data.csv"

# specify devices to process (from local/S3), DBC files, start time and optionally passwords
devices = ["LOG/2F6913DB"]
dbc_paths = ["dbc_files/ev6-gps.dbc"]
start = datetime(year=2020, month=1, day=1, hour=0, tzinfo=timezone.utc)
stop = datetime(year=2030, month=1, day=1, hour=0, tzinfo=timezone.utc)
pw = {"default": "password"}
res = "5S"

skipped_log_files = []
is_file_new = True
signals_required = inp.signals_required
signals_required.sort()

# delete output file if it exists
if os.path.exists(output_file_name):
    os.remove(output_file_name)


# setup filesystem (local/S3), load DBC files and list log files for processing
fs = setup_fs(s3=False, key="", secret="", endpoint="", region="", passwords=pw)
db_list = load_dbc_files(dbc_paths)
log_files = canedge_browser.get_log_files(
    fs, devices, start_date=start, stop_date=stop, passwords=pw
)
print(f"Found a total of {len(log_files)} log files")

# --------------------------------------------
# perform data processing of each log file (e.g. evaluation of signal stats vs. thresholds)
proc = ProcessData(fs, db_list, signals=signals_required)

for log_file in log_files:
    print(log_file)
    df_raw, device_id = proc.get_raw_data(log_file, passwords=pw)

    # remove all entries from CAN 9 (as the Epoch message overlaps with the CANmod.gps Attitude message)
    df_raw = df_raw[df_raw["BusChannel"].isin(included_bus_channels)]

    if df_raw.empty:
        continue

    tp = MultiFrameDecoder(tp_type)
    df_raw = tp.combine_tp_frames(df_raw)
    df_phys = proc.extract_phys(df_raw)

    # restructure extracted data, resample it and compare extracted signals vs. required list
    df_phys = restructure_data(df_phys=df_phys, res=res)

    signals_extracted = list(df_phys)
    signals_extracted.sort()

    if signals_extracted != signals_required:
        # print("warning: Not processed", signals_extracted)
        skipped_log_files.append({"file": log_file, "rows": len(df_phys.index)})
        continue

    # add log file name to column
    df_phys["log_file"] = log_file
    log_file_name = log_file.split("/")[-1]

    # if you prefer to use individual CSV files, you can use below:
    # df_phys.to_csv(f"{log_file_name}.csv")

    # write decoded data to csv
    if is_file_new:
        df_phys.to_csv(output_file_name, sep=",", index=True)
        is_file_new = False
    else:
        df_phys.to_csv(output_file_name, sep=",", mode="a", header=False, index=True)

print("-----------------")
print(f"Skipped {len(skipped_log_files)} log files:\n", skipped_log_files)
