import math
import warnings
from math import atan2

values = [10, 21, 25, 32]
squares = [x ** 2 for x in values]
# print(squares)

squares2 = [x ** 2 for x in values if x < 30]
# print(squares2)

squares_set = {x ** 2 for x in values}
print(squares_set)

squares_dict = {x: x ** 2 for x in values}
print(squares_dict)

total = sum([x ** 2 for x in values])
print(total)

total = sum(x ** 2 for x in values)
print(total)


# 使用警告
def waring_number(m):
    if not 1 <= m <= 12:
        msg = f'month {m} is not between 1 and 12'
        warnings.warn(msg)
waring_number(13)


# try exception
while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print("log10({0}) = {1}".format(x, y))
    except ValueError:
        print("Please enter a number")


# 返回多值
def to_polar(x, y):
    x = (x ** 2 + y ** 2) ** 0.5
    theta = atan2(y, x)
    return x, theta


a, b = to_polar(3, 5)


# print(a, b)


# 定义不定函数
def foo(x, *args):
    total = x
    for arg in args:
        total += arg
    return total


totalSum = foo(1, 2, 3, 4, 5)


# print(totalSum)


def add(x, **kwargs):
    total = x
    for key, value in kwargs.items():
        print(f"adding :{key}")
        total += value
    return total

# print(add(21, c=3, y=4, z=5))
