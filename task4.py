""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
 """

n = int(input('Введите число: '))


def get_binary_view(num):
    if num <= 0.9:
        return
    get_binary_view(num / 2)
    print(int(num % 2))


get_binary_view(n)
