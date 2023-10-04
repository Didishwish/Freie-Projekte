pages = int(input())
per_hour = int(input())
days = int(input())

time_book = pages / per_hour
hours = time_book / days

print(f'{hours: .0f}')
