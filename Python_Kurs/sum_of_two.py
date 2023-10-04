start_num = int(input())
end_num = int(input())
magic_num = int(input())

combination_no = 0
break_condition = False

for num1 in range(start_num, end_num + 1):
    for num2 in range(start_num, end_num + 1):
        combination_no += 1

        if num1 + num2 == magic_num:
            break_condition = True
            print(f'Combination N:{combination_no} ({num1} + {num2} = {magic_num})')
            break

    if break_condition:
        break

if not break_condition:
    print(f'{combination_no} combinations - neither equals {magic_num}')
