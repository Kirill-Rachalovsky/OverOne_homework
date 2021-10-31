def f(x):

    def first_interval(x):
        return 1 - (x + 2) ** 2

    def second_interval(x):
        return (-1) * (x / 2)

    def thirt_interval(x):
        return (x - 2) ** 2 + 1

    if x <= -2:
        return first_interval(x)
    elif x <= 2:
        return second_interval(x)
    else:
        return thirt_interval(x)


print(f(4.5))