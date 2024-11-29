import numpy as np


def f(x):
    return np.exp(x ** 2 + 1) + x


a = 0.2
b = 1.2
n = 10


def rectangle_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h / 2, b - h / 2, n)
    return h * np.sum(f(x))


def simpsons_rule(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    integral = h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]) + y[-1])
    return integral


integral_rect = rectangle_rule(f, a, b, n)
integral_simps = simpsons_rule(a, b, n)

print("Формула прямоугольников:", integral_rect)
print("Формула Симпсона:", integral_simps)
print("Погрешность", abs(integral_rect - integral_simps))
