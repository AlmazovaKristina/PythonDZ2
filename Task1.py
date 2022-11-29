a = (input('Введите число:'))
sum = 0
for item in a:
    if item > '0' and item <= '9':
        sum = int(item) + sum
print(sum)
