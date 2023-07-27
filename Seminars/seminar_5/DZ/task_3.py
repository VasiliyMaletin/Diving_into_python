# Создайте функцию генератор чисел Фибоначчи

a = int(input('Введите число: '))


def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fib_gen(a)))
