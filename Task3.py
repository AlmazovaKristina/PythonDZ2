import random

size = int(input('Введите длину списка:'))
my_list = []
for i in range(size):
    my_list.append(random.randint(0, 1000))
print(my_list)
print(random.sample(my_list, size))
