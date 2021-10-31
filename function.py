def simple_calc(x, action, y):
    x = int(x)
    y = int(y)
    res = None
    if action == '+':
        res = x + y
    elif action[0] == '-':
        res = x - y
    elif action[0] == '*':
        res = x * y
    elif action[0] == '/':
        res = x / y
    return res


try:
    a, action, b = input('Введите выражение, через пробелы: ').split()
    print('Ответ: ',  simple_calc(a, action, b))
except ValueError:
    print('\nВыражение введено некорректно!')
    print('Выражение необходимо вводить через пробелы.')
    print("Доступные действия: '+', '-', '*', '/'.\n")

