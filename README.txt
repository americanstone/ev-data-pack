Thanks for downloading our EV data pack!

This pack contains the following:
1) MF4 log file data recorded from various electric cars
2) DBC files for decoding the data 
3) Configuration files for recording the data
4) A unique 10000 km dataset with ~100 signals from a Kia EV6
5) A DBC decoded version of the Kia EV6 dataset, used in our ChatGPT intro:
https://www.csselectronics.com/pages/chatgpt-can-bus-data-time-series-code-interpreter

You can open the MF4 log files e.g. in below software tools and use the DBC files to decode the data.

Note that some of the sample data is multiframe UDS data.
This type of data requires using our Python API / Grafana dashboard integrations to decode it to physical values. 
This is the case for the Kia EV6, Nissan Leaf and Skoda Enyaq data. Their folders contain additional details on this. 


1) asammdf GUI: Good starting point for opening, DBC decoding and plotting the data
- Introduction: https://www.csselectronics.com/screen/page/asammdf-gui-api-mdf4
- Docs & download: https://canlogger.csselectronics.com/canedge-getting-started/ce2/log-file-tools/asammdf-gui/

2) Python API: Automate the processing of the data
- Introduction: https://www.csselectronics.com/pages/python-can-bus-api
- Docs & code examples: https://canlogger.csselectronics.com/canedge-getting-started/ce2/log-file-tools/api-tools/

3) Grafana dashboards: Create custom dashboard visualizations of the data
- Introduction: https://www.csselectronics.com/screen/page/telematics-dashboard-open-source
- Docs & code examples: https://canlogger.csselectronics.com/canedge-getting-started/ce2/log-file-tools/browser-dashboards/
- OBD2 dashboard 'playground': https://grafana.csselectronics.stellarhosted.com/d/6qvL9OvMz/css-playground-obd2

4) MF4 converters: Ideal if you want to work with the log files in e.g. Vector/PEAK tools
- Introduction: https://www.csselectronics.com/screen/page/mdf4-converters-mf4-asc-csv
- Docs & code examples: https://canlogger.csselectronics.com/canedge-getting-started/ce2/log-file-tools/mdf4-converters/


If any questions, feel free to contact us: https://www.csselectronics.com/pages/contact-us

best,
CSS Electronics