number = input()
min_num = 1000000000000000000

while number != 'Stop':
    current_number = int(number)

    if current_number < min_num:
        min_num = current_number

    number = input()

print(min_num)
