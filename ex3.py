def analyze_scores(*scores):
    if not scores:
        return 0, 0, 0
    a = sum(scores)
    b = len(scores)
    return a, b, a / b
def print_report(team_name, **info):
    print('Команда:', team_name)
    for w, j in info.items():
        print(f'{w} : {j}')
print(analyze_scores(8, 10, 7, 9))
print(analyze_scores(5, 5))
print(analyze_scores())
print_report('Комета', coach='Олежэ', city='Вращенцы')
