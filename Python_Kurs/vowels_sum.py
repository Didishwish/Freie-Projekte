text = input()
count = 0

for i in text:
    if i == 'a':
      count = count + 1
    elif i == 'e':
        count = count + 2
    elif i == 'i':
        count = count + 3
    elif i == 'o':
        count = count + 4
    elif i == 'u':
        count = count + 5

print(count)
