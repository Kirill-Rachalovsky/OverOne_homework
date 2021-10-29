def simple_calc(x, action, y):
    x = int(x)
    y = int(y)
    if action == '+':
        res = 'Ответ: ' + str(x + y)
    elif action[0] == '-':
        res = 'Ответ: ' + str(x - y)
    elif action[0] == '*':
        res = 'Ответ: ' + str(x * y)
    elif action[0] == '/':
        res = 'Ответ: ' + str(x / y)
    return res



try:
    a, action, b = input('Введите выражение, через пробелы: ').split()
    print(simple_calc(a, action, b))
except ValueError:
    print('\nВыражение введено некорректно!')
    print('Выражение необходимо вводить через пробелы.')
    print("Доступные действия: '+', '-', '*', '/'.\n")
