This dataset is recorded from a new Kia EV6 over an extended period of time.

You can replicate this using a CANedge and a CANmod.gps, as well as the included Configuration File. See our Kia EV6 case study for details:
https://www.csselectronics.com/pages/kia-ev6-can-bus-data-uds-dbc

To process and decode the data, you can e.g. use the CANedge Python API / dashboard integration. 

This folder contains dashboard templates that can be used for both the 'CANedge Grafana Backend' integration and the 'CANedge InfluxDB Writer' integration.

You can revert back to the download page for the data pack periodically for an updated version of this dataset with additional data.

NOTE: This config/DBC should support more-or-less all Hyundai/Kia electric cars. In particular, this includes:
- Hyundai Kona
- Hyundai Ioniq
- Kia Niro

The DBC was based on the work from below repository:
https://github.com/JejuSoul/OBD-PIDs-for-HKMC-EVs