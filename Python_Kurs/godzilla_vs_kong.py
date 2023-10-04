budget = float(input())
extras = int(input())
price_costume_one = float(input())
price_costume_all = 0

decor_price = budget * 0.1

if extras > 150:
    price_costume_all = extras * price_costume_one - (extras * price_costume_one) * 0.1
else:
    price_costume_all = extras * price_costume_one

all_expenses = price_costume_all + decor_price

if budget < all_expenses:
    need_more = all_expenses - budget
    print('Not enough money!')
    print(f'Wingard needs {need_more:.2f} leva more.')
else:
    left = budget - all_expenses
    print('Action!')
    print(f'Wingard starts filming with {left:.2f} leva left.')
