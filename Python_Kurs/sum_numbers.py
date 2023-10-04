number = int(input())
sum_numbers = 0

while True:
    current_num = int(input())
    sum_numbers += current_num

    if sum_numbers >= number:
        print(sum_numbers)
        break

