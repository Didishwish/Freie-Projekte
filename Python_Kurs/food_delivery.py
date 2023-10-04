chicken = int(input())
fish = int(input())
veggie = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.4
veggie_price = veggie * 8.15
price_menu = chicken_price + fish_price + veggie_price
desert = price_menu * 0.2
full_price = price_menu + desert + 2.5

print(full_price)