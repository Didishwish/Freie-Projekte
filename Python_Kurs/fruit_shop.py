fruit = input()
day = input()
how_much = float(input())
price = 0

if fruit == 'banana':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 2.50
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 2.70
    print(f'{price:.2f}')
elif fruit == 'apple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 1.20
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 1.25
    print(f'{price:.2f}')
elif fruit == 'orange':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 0.85
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 0.90
    print(f'{price:.2f}')
elif fruit == 'grapefruit':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 1.45
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 1.60
    print(f'{price:.2f}')
elif fruit == 'kiwi':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 2.70
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 3.00
    print(f'{price:.2f}')
elif fruit == 'pineapple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 5.50
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 5.60
    print(f'{price:.2f}')
elif fruit == 'grapes':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        price = how_much * 3.85
    elif day == 'Saturday' or day == 'Sunday':
        price = how_much * 4.20
    print(f'{price:.2f}')
else:
    print('error')

