"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random
m = 5
size = 2*m + 1
num_list = list(set([random.randint(0, 10) for _ in range(size)]))
if len(num_list) % 2 == 0:
    num_list.append(random.randint(0, 10))


print(f"Массив исходный: {num_list}")

# Найдем медиану так, чтобы число её превышений элементами стало равно числу элементов, которые ее не больше.
def med(nums):
    length = len(nums)
    for i in range(length):
        s1, s2 = [], []
        val = nums[i]
        for j in range(length):
            if nums[j] <= val:
                s1.append(nums[j])
            if nums[j] >= val:
                s2.append(nums[j])
        print(val, s1, s2)
        if len(s1) == len(s2):
            return val


print(f"{sorted(num_list[:])}")
print(f"Медиана: {med(num_list[:])}")
