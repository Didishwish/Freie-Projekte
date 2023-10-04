fruit = input()
day = input()
how_much = float(input())
price = 0

if fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' or\
       fruit == 'kiwi' or fruit == 'pineapple' or fruit == 'grapes':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        if fruit == 'banana':
            price = how_much * 2.50
            print(f'{price:.2f}')
        elif fruit == 'apple':
            price = how_much * 1.20
            print(f'{price:.2f}')
        elif fruit == 'orange':
            price = how_much * 0.85
            print(f'{price:.2f}')
        elif fruit == 'grapefruit':
            price = how_much * 1.45
            print(f'{price:.2f}')
        elif fruit == 'kiwi':
            price = how_much * 2.70
            print(f'{price:.2f}')
        elif fruit == 'pineapple':
            price = how_much * 5.50
            print(f'{price:.2f}')
        elif fruit == 'grapes':
            price = how_much * 3.85
            print(f'{price:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        if fruit == 'banana':
            price = how_much * 2.70
            print(f'{price:.2f}')
        elif fruit == 'apple':
            price = how_much * 1.25
            print(f'{price:.2f}')
        elif fruit == 'orange':
            price = how_much * 0.90
            print(f'{price:.2f}')
        elif fruit == 'grapefruit':
            price = how_much * 1.60
            print(f'{price:.2f}')
        elif fruit == 'kiwi':
            price = how_much * 3.00
            print(f'{price:.2f}')
        elif fruit == 'pineapple':
            price = how_much * 5.60
            print(f'{price:.2f}')
        elif fruit == 'grapes':
            price = how_much * 4.20
            print(f'{price:.2f}')
    else:
        print('error')
else:
    print('error')
