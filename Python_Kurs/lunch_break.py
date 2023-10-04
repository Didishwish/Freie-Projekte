from math import ceil

series = input()
length = int(input())
lunch_break = int(input())

eating = lunch_break / 8
walk = lunch_break / 4

time_used = eating + walk + length
time_left = lunch_break - time_used

if time_left >= 0:
    print(f"You have enough time to watch {series} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(abs(time_left))} more minutes.")
