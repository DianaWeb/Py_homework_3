""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 10.01] => 0.19 """
nums = [1.1, 1.2, 3.1, 10.01]
nums_2 = []

for i in range(len(nums)):
    n = round((nums[i] % 1), 2)
    nums_2.append(n)
print(nums_2)

minn = min(nums_2)
print(minn)
maxx = max(nums_2)
print(maxx)
res = maxx - minn
print(res)
