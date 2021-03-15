# Description of the logs

This directory contains log files from sensors, in different elevators.

Each file hast 2 number in it, the first one is the sensor ID, the second one is the location.
e.g. `log_raw_04.dat.1` is from sensor `04` and location `1` 

All sensors have the same firmware and store the raw data in the log file.
The data is triggered by an interrupt and then fills the log with 32 consecutive values.
The sampling rate is aprrox. 75Hz.

## Data structure

The data has the following structure:
```
[time_s],[time_us],[raw_acc_G_0],[raw_acc_G_1], ... ,[raw_acc_G_31]
[time_s],[time_us],[raw_acc_G_0],[raw_acc_G_1], ... ,[raw_acc_G_31]
...
[time_s],[time_us],[raw_acc_G_0],[raw_acc_G_1], ... ,[raw_acc_G_31]
```

## Locations and movements
- 1: **Alnatura** 
    - Manufacturer: unknown
    - movement: (0) -> (-2) -> (0) -> (-2) -> (-1) -> 0
    
- 2: **Edeka**
    - Manufacturer: Kone
    - movement: (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0)
    
- 3: **Bauhaus**
    - Manufaturer: Walter Meyer Hydraulic
    - movement: (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0)

- 4: **Mainstation** Gl. 2+3
    - Manufacturer: OTIS
    - movement: (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0)
    
- 5: **Mainstation** Gl. 4+5
    - Manufacturer: OTIS
    - movement: (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0)

- 6: **Mainstation** Gl. 6+7
    - Manufacturer: OTIS
    - movement: (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0)

- 7: **Grether**
    - Manufaturer: Aufzug Hebelzeug
    - movement: (0) -> (1) -> (2) -> (3) -> (4) -> (3) -> (2) -> (1) -> (0) -> (4) -> (3) -> (4) -> (3) -> (4) -> (0)
    
- 8: **Marie-Curie34**
    - Manufaturer: unknown
    - movement: (2) -> (-1) -> (4) -> (-1) -> (2) -> (-1) -> (0) -> (1) -> (2) -> (3) -> (4) -> (3) -> (2) -> (1) -> (0)
    
- 9: **REWE**
    - Manufacturer: unknown
    - movement: (1) -> (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0) -> (1) -> (0)
