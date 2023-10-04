budget = float(input())
graphic_card = int(input())
processor = int(input())
ram = int(input())
paying = 0

price_graphic = graphic_card * 250
price_processor = processor * (price_graphic * 0.35)
price_ram = ram * (price_graphic * 0.1)

end_price = price_graphic + price_processor + price_ram

if graphic_card > processor:
    paying = end_price - (end_price * 0.15)
else:
    paying = end_price

if paying <= budget:
    rest = budget - paying
    print(f'You have {rest:.2f} leva left!')
else:
    need = paying - budget
    print(f'Not enough money! You need {need:.2f} leva more!')
