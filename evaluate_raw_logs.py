#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pytz
from datetime import datetime

import sensor as sensor

USED_TIMEZONE = pytz.timezone('Europe/Berlin')#pytz.utc

def convert_timestamps(timestamps_in):
    return [datetime.fromtimestamp(ts,USED_TIMEZONE) for ts in timestamps_in]


FILE = "rawData/log_raw_00.dat.8"
timestamp_s_raw = []
timestamp_us_raw = []
accel_raw = []
timestamp_us = []
timecount = []
timedelta = []

# read the input file and store the values into buffers
with open (FILE, 'r') as f:
    count = 0
    buffer_pre = 0
    buffer_post = 0
    while True:
        count += 1
        # Get next line from file
        line = f.readline().rstrip('\n').rstrip(',')
        # if line is empty
        # end of file is reached
        if not line:
            break
        line_list = line.split(",",maxsplit=34)
        if len(line_list) >2:
            timestamp_s_raw.append(int(line_list[0]))
            timestamp_us_raw.append(int(line_list[1]))
            buffer_post = timestamp_us_raw[-1]   # take the last value
            for i in range(2,len(line_list)):
                accel_raw.append(float(line_list[i]))
                timestamp_us.append(int((buffer_post -buffer_pre) / 32.0 * (i-2) + buffer_pre))

        timecount.append(count)
        timedelta.append(buffer_post - buffer_pre)
        buffer_pre = buffer_post # stores the value for the next round
    #    print("Line{}: {}".format(count, line.strip()))

# print("timestamp_s_raw ({}) = {}".format(len(timestamp_s_raw), timestamp_s_raw))
# print("timestamp_us_raw ({}) = {}".format(len(timestamp_us_raw), timestamp_us_raw))
# print("timestamp_us ({}) = {}".format(len(timestamp_us), timestamp_us))
# print("accel_raw ({}) = {}".format(len(accel_raw),accel_raw))

# print(timestamp)



# convert to numpy
_ts = np.array(timestamp_us[:len(timestamp_us)])
_td = np.array(timedelta[:len(timedelta)])
_ar = np.array(accel_raw[:len(accel_raw)])

# time = np.array(timecount[:len(timecount)])
time = convert_timestamps(_ts)

# plot results
# plt.plot(time, _ts, '-', label='X')
plt.subplot(211)
plt.plot(time, _ar, '-', label='delta')

plt.xlabel('Time [ms]')
plt.ylabel('Acceleration [G]')
plt.grid()
plt.legend()

# plt.show()

# now do the filtering
x1_points = accel_raw
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
# time = convert_timestamps(time)
x = np.array(x1_points)


# plot results
plt.subplot(212)
plt.plot(time, x, '-', label='X')
plt.plot(time, _as[0], '-', label='AS')
# plt.plot(time, _af[0], '-', label='AF')
plt.plot(time, _afs[0], '-', label='AFS')
plt.plot(time, _s[0], '-', label='S')
plt.plot(time, _ss[0], '-', label='SS')
plt.plot(time, _sf[0], '-', label='SF')
plt.plot(time, _sfs[0], '-', label='SFS')


plt.xlabel('Time [s]')
plt.ylabel('Acceleration [mG]')
plt.grid()
plt.legend()

plt.show()
