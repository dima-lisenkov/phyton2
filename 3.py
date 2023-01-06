n = int(input('Введите число n: '))
result = []
sum = 0
for i in range(1, n + 1):
    result.append(round((1 + 1/i)**i, 2))
    sum += result[i - 1]
print(f'Для n={n} -> {result}')
print(f'Сумма {round(sum,2)}')