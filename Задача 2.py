def factorial (number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

n = int(input('Введите число: '))
print(f'Set of products of numbers from 1 to {n} = ', end = '')
for i in range(1, n + 1):
    if i == n: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')