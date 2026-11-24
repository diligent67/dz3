def average_grade(a, b, c):
    return (a + b + c) / 3
def grade_message(average):
    if average < 3.5:
        return 'Нужно повторить материал'
    elif average < 4.5:
        return 'Хорошо'
    else:
        return 'Отлично'
print(round(average_grade(5, 4, 5), 2), grade_message(average_grade(5, 4, 5)))
print(round(average_grade(3, 4, 3), 2), grade_message(average_grade(3, 4, 3)))
