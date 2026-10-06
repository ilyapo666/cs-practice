def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def pr(a,b):
    return a*b
def div(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
print(f"Результат сложения: {add(a,b)}")
print(f"Результат вычитания: {minus(a,b)}")
print(f"Результат умножения: {pr(a,b)}")
