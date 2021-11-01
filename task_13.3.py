def transformation(lst):
    for i in lst:
        if i % 2 == 1:
            lst.remove(i)
        else:
            lst[lst.index(i)] = int(i/2)
    return lst


print(transformation([852, 85, 784, 58]))


