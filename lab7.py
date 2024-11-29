import numpy as np


def f(x):
    return x**2


def rect_int(func, a, b, n):
    h = (b - a) / n
    res = []
    ans = 0
    for i in range(n):
        left = a + h * i
        right = a + h * (i + 1)
        center = (left + right) / 2
        ans += func(left) * h
        res.append(func(left) * h)

    print(res)
    # for x in np.array(res):
    #     print(f"{x:.5f}")
    return ans


def simpson_int(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    integral = h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]) + y[-1])
    return integral


a = 0
b = 1
n = 10

integral_rect = rect_int(f, a, b, n)
integral_simps = simpson_int(a, b, n)


print("  ")
print("Формула прямоугольников:",  f"{integral_rect:.5f}")
print("Формула Симпсона:", f"{integral_simps:.5f}")
print("Погрешность", f"{abs(integral_rect - integral_simps):.5f}")
