dep_sum = float(input())
months = int(input())
interest = float(input())

per_months = interest / 100
full_interest = dep_sum * per_months
interest_months = full_interest / 12
all_sum = dep_sum + months * interest_months

print(all_sum)
