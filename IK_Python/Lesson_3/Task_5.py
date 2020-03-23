"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random
num_list = list(set([random.randint(-20, 20) for _ in range(0, 10)]))
print(f"Массив: {num_list}")
neg_dict = {el: i for i, el in enumerate(num_list) if el < 0}
maximum = list(neg_dict.keys())[0]
for key, val in neg_dict.items():
    if key > maximum:
        maximum = key
print(f"Максимальный отрицательный элемент: {maximum}, позиция: {neg_dict.get(maximum)}")
