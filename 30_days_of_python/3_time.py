# 17 April 2023
# By Ruddy Starr 
# Day 3 of 100 Days of Coding & Day 3 of 30 Days of Python
# Program to convert an amount of minutes into an equivalent amount
# of days, hours and minutes.

# prompt user for input
prompt = eval(input("Enter a quantity of minutes: "))

# time conversions
minutes = prompt
minutes = minutes%60
hours = minutes//60
hours = hours%60
days = hours//24

# print out conversion
print("The number of days is {0}, the number of hours is {1} and the number of minutes is {2}.".format(days, hours, minutes))

