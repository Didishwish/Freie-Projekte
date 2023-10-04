pens = int(input())
markers = int(input())
litres = int(input())
discount = int(input()) / 100

pens_price = 5.80
markers_price = 7.2
litres_price = 1.2

price_before_discount = \
    (pens_price * pens) + \
    (markers_price * markers) + \
    (litres * litres_price)
full_price = price_before_discount - price_before_discount * discount

print(full_price)