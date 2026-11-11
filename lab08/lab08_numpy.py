import numpy as np

print("--- Задание 1. Создание векторов и матриц ---")
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)

print("\n--- Задание 2. Индексы и срезы в векторе ---")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

print("\n--- Задание 3. Строки и столбцы таблицы ---")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape, "Число измерений:", temperatures.ndim, "Элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0, :])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[0:2, 1:3])

print("\n--- Задание 4. Прямоугольные срезы ---")
matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная матрица:\n", matrix)

first_3_rows = matrix[:3, :]
print("\nПервые три строки:\n", first_3_rows, "\nshape:", first_3_rows.shape)

last_2_rows = matrix[-2:, :]
print("\nПоследние две строки:\n", last_2_rows, "\nshape:", last_2_rows.shape)

first_2_cols = matrix[:, :2]
print("\nПервые два столбца:\n", first_2_cols, "\nshape:", first_2_cols.shape)

fragment_1_3_2_4 = matrix[1:4, 2:5]
print("\nФрагмент (строки 1-3, столбцы 2-4):\n", fragment_1_3_2_4, "\nshape:", fragment_1_3_2_4.shape)

bottom_right = matrix[-2:, -2:]
print("\nУгловой блок 2x2 в правом нижнем углу:\n", bottom_right, "\nshape:", bottom_right.shape)

print("\n--- Задание 5. Изменение массива с помощью срезов ---")
# Примеры из задания
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# Изменение hours
changed_hours = hours.copy()
# .copy() нужен для того, чтобы изменения в changed_hours не затронули исходный массив hours. 
# Если написать changed_hours = hours, то обе переменные будут ссылаться на один и тот же объект в памяти.
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

# Изменение matrix
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("\nchanged_matrix:\n", changed_matrix)
print("\nИсходная matrix:\n", matrix)

print("\n--- Задание 6. Изменение формы ---")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)


