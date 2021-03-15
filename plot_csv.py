import csv
import matplotlib.pyplot as plt
import numpy as np
import pytz
from datetime import datetime

import sensor as sensor

USED_TIMEZONE = pytz.timezone('Europe/Berlin')#pytz.utc 

def convert_timestamps(timestamps_in):
    return [datetime.fromtimestamp(ts,USED_TIMEZONE) for ts in timestamps_in]


# CSV file with the input acceleration values: ts[s],x[mg],y[mg],z[mg]
INPUT_FILENAME = "received_data.csv"

# set up variables for loading data
x1_points = []
y1_points = []
z1_points = []
timepoints = []

ROW_INDEX_TIME = 0
ROW_INDEX_X1 = 1
ROW_INDEX_Y1 = 2
ROW_INDEX_Z1 = 3

# load the data from file
with open(INPUT_FILENAME, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        x1_points.append(int(row[ROW_INDEX_X1]))
        y1_points.append(int(row[ROW_INDEX_Y1]))
        z1_points.append(int(row[ROW_INDEX_Z1]))
        timepoints.append(float(row[ROW_INDEX_TIME])) # float type subsecond timestamp

from generate_input_data import read_data

#x1_points = read_data("step25.txt")
#x1_points = read_data("step13.txt")
#x1_points = read_data("jump.txt")
#x1_points = read_data("random.txt")
#x1_points = read_data("jump_60_rand_60.txt")
#x1_points = read_data("jump_60_rand_120.txt")
#x1_points = read_data("jump_60_rand_200.txt")
x1_points = read_data("real_jump_60_rand_200.txt")


timepoints = read_data("time.txt")

#######################################
# get the sensor filters and variables
sensor = sensor.MovementSensor()

accel_smooth = []
accel_filtered = []
accel_filtered_smooth = []
speed = []
speed_smooth = []
speed_filtered = []
speed_filtered_smooth = []

for j in range(3):
    accel_smooth.append([])
    accel_filtered.append([])
    accel_filtered_smooth.append([])
    speed.append([])
    speed_smooth.append([])
    speed_filtered.append([])
    speed_filtered_smooth.append([])

#########################################
# forward the data to the filters
for x in range(0, len(x1_points), 32):
    sensor.write_sensor_values(x1_points[x+0:x+32], x1_points[x+0:x+32], x1_points[x+0:x+32])
    sensor.calc_speed()

    for j in range(3):
        for i in range(32):
            accel_smooth[j].append(sensor.accel_smooth[i][j])
            accel_filtered[j].append(sensor.accel_filtered[i][j])
            accel_filtered_smooth[j].append(sensor.accel_filtered_smooth[i][j])
            speed[j].append(sensor.speed[i][j])
            speed_smooth[j].append(sensor.speed_smooth[i][j])
            speed_filtered[j].append(sensor.speed_filtered[i][j])
            speed_filtered_smooth[j].append(sensor.speed_filtered_smooth[i][j])

# convert to numpy
_as = np.array(accel_smooth[:len(x1_points)])
_af = np.array(accel_filtered[:len(x1_points)])
_afs = np.array(accel_filtered_smooth[:len(x1_points)])
_s = np.array(speed[:len(x1_points)])
_ss = np.array(speed_smooth[:len(x1_points)])
_sf = np.array(speed_filtered[:len(x1_points)])
_sfs = np.array(speed_filtered_smooth[:len(x1_points)])

# convert to numpy arrays
time = np.array(timepoints[:len(x1_points)])
time = convert_timestamps(time)
x = np.array(x1_points)
y = np.array(y1_points)
z = np.array(z1_points)

# plot results
plt.plot(time, x, 'x-', label='X')
plt.plot(time, _as[0], 'x-', label='AS')
# plt.plot(time, _af[0], 'x-', label='AF')
plt.plot(time, _afs[0], 'x-', label='AFS')
plt.plot(time, _s[0], 'x-', label='S')
plt.plot(time, _ss[0], 'x-', label='SS')
plt.plot(time, _sf[0], 'x-', label='SF')
plt.plot(time, _sfs[0], 'x-', label='SFS')


plt.xlabel('Time [s]')
plt.ylabel('Acceleration [mG]')
plt.grid()
plt.legend()

plt.show()