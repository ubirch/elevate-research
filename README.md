# Elevate Research Scripts

This repository is used for research purposes to get a better understanding of 
the sensor behaviour and also to develop a filter or the raw elevator data.
This filter shall be able to determine, if an elevator is moving, while at the
same time not get triggered, if somebody is entering the elevator, but the 
elevator itself is not moving.

## Script files
- [sensor.py](sensor.py) represents the sensor and the filtering algorithm of 
the implemented sensor in the [elevate Application](https://github.com/ubirch/ubirch-elevate-application)
  which is used unmodified for the data filtering and movement recognition
  
- [evaluate_row_logs.py](evaluate_raw_logs.py) is used to read the data from
the logs, which can be found in [rawData](rawData/README.md) and applies the
  filter to it.
  
- [generate_input_data.py](generate_input_data.py) can generate different input
data for the filters.
  
- [plot_csv.py](plot_csv.py) is used ta apply the filtering on data from 
[generate_input_data.py](generate_input_data.py)
  
