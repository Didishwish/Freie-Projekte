import math
record = float(input())
metres = float(input())
time_metre = float(input())

time = time_metre * metres
end_time = 0

if metres >= 15:
    slower_how = metres // 15
    math.floor(slower_how)
    slower = slower_how * 12.5
    end_time = time + slower
else:
    end_time = time

if end_time < record:
    print(f'Yes, he succeeded! The new world record is {end_time:.2f} seconds.')
else:
    difference = end_time - record
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
