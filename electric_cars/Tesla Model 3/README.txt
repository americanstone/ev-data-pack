This dataset is recorded from a Tesla Model 3 (2019).

You can replicate this using a CANedge and the included Configuration File (the default CANedge config will work).

For details on the implementation, see our case study:
https://www.csselectronics.com/pages/tesla-data-dashboard-telematics-can-bus-grafana

To process and decode the data, you can e.g. use the asammdf GUI or the CANedge Python API / dashboard integration. 
Note that no multiframe decoding is required here as the data is broadcast by the Tesla, not only available on-request.

This folder contains dashboard templates that can be used for the 'CANedge InfluxDB Writer' integration.

NOTE: This config/DBC should support more-or-less all Tesla electric cars.

The DBC was based on the work from below repository:
https://github.com/joshwardell/model3dbc