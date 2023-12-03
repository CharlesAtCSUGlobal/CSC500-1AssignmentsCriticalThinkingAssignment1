# Charles Henrikson
#
# 23WA-CSC500-1
# Module 3: Critical Thinking Assignment
# Part 2:

# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13, and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.


print("Welcome to Hourly Alarm!")

# Collect data
current_hours = int(input("What is the time now (in hours)? "))
num_wait_hours = int(input("How many hours to wait until the alarm? "))

# Calculate Alarm
alarm_time = (num_wait_hours + current_hours) % 24

# Calculate 12 hour time
twelve_hour_clock_time = 0
twelve_hour_type = ''
if alarm_time > 11:
    twelve_hour_type = 'pm'
else:
    twelve_hour_type = 'am'
if alarm_time > 12:
    twelve_hour_clock_time = alarm_time - 12
else:
    twelve_hour_clock_time = alarm_time

# Print Alarm

print('\nIf it is currently {}, and you set your alarm to go off in {} hours, it will be {} ({}{})'.format(current_hours, num_wait_hours, alarm_time, twelve_hour_clock_time, twelve_hour_type))
