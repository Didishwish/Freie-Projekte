price_year = int(input())

price_sneakers = price_year - (price_year * 0.4)
price_clothes = price_sneakers - (price_sneakers * 0.2)
price_ball = price_clothes / 4
price_accessoires = price_ball / 5

price_all = price_year + price_sneakers + price_clothes + price_ball + price_accessoires

print(price_all)