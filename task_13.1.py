def list_of_sum(lst):
    sum_list = []
    for number in lst:
        summ = 0
        while number:
            summ += number % 10
            number = number // 10
        sum_list.append(summ)
    return sorted(sum_list)


list_of_numbers = [int(i) for i in input().split()]

print(list_of_sum(list_of_numbers))