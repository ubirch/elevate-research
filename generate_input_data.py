"""
file to generate input data for the filters
"""
import random
import math

def read_data(filename):
    with open(filename, "r") as f:
        reader = f.read()

#    print("reader = {}".format(reader))
    reader = reader.lstrip("[").rstrip("]")
    reader_int = reader.split(",")
#    print("reader_int = {}".format(reader_int))

    reader_list = []
    for i in range(len(reader_int)):
        if reader_int[i].__contains__('.'):
            reader_list.append(float(reader_int[i]))
        else:
            reader_list.append(int(reader_int[i]))

    return reader_list


FILENAME = "jump.txt"
jump = []

for i in range(1024):
    jump.append(0.0)

for i in range(3072):
    jump.append(0.6/9.81)

with open(FILENAME, "w") as f:
    f.write(str(jump))

##########################################
# generate timestamps with 75 values per second
FILE_TIME = "time.txt"
time = []
for i in range(4096):
    time.append(i/75.0)

with open(FILE_TIME, "w") as f:
    f.write(str(time))

############################################
# generate a step of 61 mg for 2,5 seconds and -61 mg later
FILENAME_STEP25 = "step25.txt"
step = []

for i in range(1024):
    step.append(0.0)
for i in range(187): # 187
    step.append(0.6/9.81)
for i in range(1024):
    step.append(0.0)
for i in range(187):
    step.append(-0.61/9.81)
for i in range(2048-187 -187):
    step.append(0.0)

with open(FILENAME_STEP25, "w") as f:
    f.write(str(step))
del step

############################################
# generate a step of 61 mg for 2,5 seconds and -61 mg later
FILENAME_STEP25 = "step13.txt"
step = []

for i in range(1024):
    step.append(0.0)
for i in range(32): # 187
    step.append(0.6/9.81)
for i in range(1024):
    step.append(0.0)
for i in range(32):
    step.append(-0.6/9.81)
for i in range(2048-32-32):
    step.append(0.0)

with open(FILENAME_STEP25, "w") as f:
    f.write(str(step))

############################################
FILENAME_RANDOM = "random.txt"
randooom = []

for i in range(1024):
    randooom.append(0.0)
for i in range(2048):
    randooom.append(random.randint(-4096, 4096)/4096*(2.4/9.81))
for i in range(1024):
    randooom.append(0.0)

with open(FILENAME_RANDOM, "w") as f:
    f.write(str(randooom))

############################################
FILENAME_RANDOM = "real_jump_60_rand_200.txt"
randooom2 = []

RAUSCHEN = 0
AMPLI = 0.61
DAUER = int(1.0 * 73)

for i in range(1024):
    randooom2.append(0)
for i in range(DAUER):
    randooom2.append(AMPLI/9.81)
for i in range(2048):
    randooom2.append(0)
for i in range(DAUER):
    randooom2.append(-AMPLI/9.81)
for i in range(1024 - DAUER - DAUER):
    randooom2.append(0)

RAUSCHEN2 = 1/9.81
PER = 10
AMPL = 0/9.81
OFFS = 0/9.81

for i in range(len(randooom2)):
    randooom2[i] += math.sin((i/PER)%(2*math.pi))*AMPL +OFFS
    randooom2[i] += random.randint(-4096, 4096)/4096*(RAUSCHEN2)

with open(FILENAME_RANDOM, "w") as f:
    f.write(str(randooom2))

# for i in range()


reader_list = read_data(FILENAME)



# print("Length: {} Type: {}".format(len(reader), type(reader)))
# print("Length: {} Type: {}".format(len(reader_int), type(reader_int)))
# print("Length: {} Type: {}".format(len(reader_list), type(reader_list)))

# print(reader_list)

