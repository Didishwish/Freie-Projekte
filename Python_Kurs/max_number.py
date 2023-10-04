number = input()
max_num = -1000000000000000000

while number != 'Stop':
    current_number = int(number)

    if current_number > max_num:
        max_num = current_number

    number = input()

print(max_num)
