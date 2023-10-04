lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = lenght * width * height
volume_litres = volume * 0.001
percent_num = percent / 100
litres = volume_litres * (1 - percent_num)

print(litres)
