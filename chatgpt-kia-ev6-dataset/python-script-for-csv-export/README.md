# Combine multiple MF4 files into single CSV
This script is used to go through multiple MF4 files, DBC decode them and produce a single CSV file output.

The script is set up to be used with the Kia EV6 data from this EV data pack - but it can be modified easily for other use cases.

## Installation
This script takes outset in our api-examples script for the CANedge Python API - we recommend seeing that for installation guidance and `requirements.txt` files:
https://github.com/CSS-Electronics/api-examples

## Adding data
You can run the script with the default data in this folder, or you can copy the entire EV6 dataset into the LOG folder.

## Adding your own MF4 files 
If you want to use this script with your own log files, you'll need to modify the following:

In `inputs.py`:
- Change the `signals_require` list to the list you require to be included in every log file

In `main.py`:
- Set `tp_type = ""` unless you need to process multiframe data 
- Set `included_bus_channels` to include `9` if you wish to process the internal GNSS/IMU data of a CANedge 
- Update `devices` and `dbc_paths` and optionally `start` and `stop`