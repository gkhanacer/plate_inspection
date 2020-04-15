#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

# Chage times (minute)
charge_times = [30, 45, 60, 75, 90, 105, 120, 135, 150]

# Total cleaning time WHEN HAS INFINITY ENERGY (minute)
cleaning_times_inf = [30, 45, 60, 75, 90, 105, 120, 135, 150]

# Cleaning time for robot's 1-iteration 
cleaning_times = [30, 45, 60, 75, 90, 105, 120, 135, 150]

dict_data = []

def calc_ttc(charge_time, celaning_time_inf, cleaning_time):
    tct = 0
    remaining_time = celaning_time_inf
    while remaining_time > 0:
        tct = tct + cleaning_time
        tct = tct + charge_time
        remaining_time = remaining_time - cleaning_time

    tct = tct + remaining_time - charge_time
    print("Charge Time: {}, Cleaning Time Infinity: {}, Cleaning Time for 1-Iteration: {}, Total Cleaning Time (TCT) {}".format(charge_time, celaning_time_inf, cleaning_time, tct))
    # print("Remaining Time {}".format(remaining_time))
    dict_data.append({'Charge Time' : charge_time, 'Cleaning Time Infinity': celaning_time_inf, 'Cleaning Time for 1-Iteration': cleaning_time, 'Total Cleaning Time (TCT)': tct})

for charge_time in charge_times:
    for celaning_time_inf in cleaning_times_inf:
        for cleaning_time in cleaning_times:
            calc_ttc(charge_time, celaning_time_inf, cleaning_time)

# # TEST
# charge_time = charge_times[2]               # 60 min
# celaning_time_inf = cleaning_times_inf[2]   # 60 min
# cleaning_time = cleaning_times[2]            # 60 min
# calc_ttc(charge_time, celaning_time_inf, cleaning_time)

# # TEST
# charge_time = charge_times[2]               # 60 min
# celaning_time_inf = cleaning_times_inf[3]   # 75 min
# cleaning_time = cleaning_times[2]            # 60 min
# calc_ttc(charge_time, celaning_time_inf, cleaning_time)

csv_file = "Result.csv"
csv_columns = ['Charge Time', 'Cleaning Time Infinity', 'Cleaning Time for 1-Iteration', 'Total Cleaning Time (TCT)']
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")