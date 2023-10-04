price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price_toys = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2

all_toys = puzzles + dolls + bears + minions + trucks

if all_toys >= 50:
    end_price = price_toys - (price_toys * 0.25)
else:
    end_price = price_toys

profit = end_price - (end_price * 0.1)

if price <= profit:
    left = profit - price
    print(f'Yes! {left:.2f} lv left.')
else:
    needed = price - profit
    print(f'Not enough money! {needed:.2f} lv needed.')
