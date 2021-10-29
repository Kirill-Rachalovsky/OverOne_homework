def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def mult(a, b):
    return a * b


def division(a, b):
    return a / b


while True:

    try:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        action = input("Выберете действие ('+', '-', '*', '/'):  ")
    except ValueError:
        print('Данные введены некорректно. Повторите попытку.')
        continue

    if action[0] == '+':
        print('Ответ:', addition(x, y), '\n')
    elif action[0] == '-':
        print('Ответ:', subtraction(x, y), '\n')
    elif action[0] == '*':
        print('Ответ:', mult(x, y), '\n')
    elif action[0] == '/':
        print('Ответ:', division(x, y), '\n')

    end = input("Желаете продолжить? (y/n) \n")
    if end == 'n':
        break
