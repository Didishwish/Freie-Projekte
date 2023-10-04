student_name = str(input())
grades_total = 0
years = 0
failed = 0

while True:
    current_year_grade = float(input())

    if current_year_grade < 4:
        failed += 1
        if failed == 2:
            print(f'{student_name} has been excluded at {years + 1} grade')
            break
    else:
        years += 1
        grades_total += current_year_grade

        if years == 12:
            average_grade = grades_total / 12
            print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
            break
