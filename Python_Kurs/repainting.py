nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_materials = (nylon + 2) * 1.5 + (paint + paint / 10) * 14.5 + thinner * 5 + 0.4
price_work = (price_materials * 0.3) * hours
end_price = price_materials + price_work

print(end_price)
