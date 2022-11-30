import random


def summa(x):
    summa_result = 0
    for c in x:
        summa_result = summa_result + int(c)
    return summa_result


def final_summa(x):
    fs = summa(x)
    while fs > 9:
        fs = summa(str(fs))
    return fs


def check(list_1, element):
    for d in list_1:
        if d == element:
            return False
    return True


size = int(input('Введите длину списка: '))
my_list = []
for i in range(size):
    my_list.append(random.randint(999, 9999))
print(my_list)

a = (input('Введите цифру: '))

result = []
for item in my_list:
    s = str(item)
    result.append(s.replace(a, ''))
print(result)

result3 = []
for e in result:
    result3.append(final_summa(e))
print(result3)

result4 = []
for e in result3:
    if check(result4, e):
        result4.append(e)

print(result4)

