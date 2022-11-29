size = int(input('Введите количество чисел:'))
my_list = []
sum = 0
for i in range(size):
    my_list.append((1 + 1 / (i + 1)) ** (i + 1))
    sum = sum + my_list[i]
print(my_list)
print(sum)
