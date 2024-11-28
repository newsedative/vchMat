'''
  def f(x):
    return x ** 2


def rect_int(func, a, b, n=1000):
    h = (b - a) / n
    ans = 0
    for i in range(n):
        x1 = a + h * i
        x2 = a + h * (i + 1)
        c = (x1 + x2) / 2
        ans += func(c) * h
    return ans


def simpson_int(func, a, b, n=1000):
    n += n % 2
    h = (b - a) / n
    y = [f(a + i * h) for i in range(n + 1)]
    m = n // 2
    ans = (y[0] + y[2 * m] + 4 * y[1]) * h / 3
    for i in range(2, m + 1):
        ans += (4 * y[2 * i - 1] + 2 * y[2 * i - 2]) * h / 3
    return ans


print(rect_int(f, 1, 2))
print(simpson_int(f, 1, 2))
'''


import numpy as np

def f(x):
  return np.exp(x**2 + 1) + x

a = 0.2
b = 1.2
n = 10

def rectangle_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a + h/2, b - h/2, n)
  return h * np.sum(f(x))

def trapezoid_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a, b, n + 1)
  y = f(x)
  return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

integral_rect = rectangle_rule(f, a, b, n)
integral_trap = trapezoid_rule(f, a, b, n)

print("Формула треугольников:", integral_rect)
print("Формула трапеций:", integral_trap)

h_rect = (b-a)/n
approx_error_rect = (b-a) * abs(f(1) - f(0)) * (h_rect)**2 /24



h_trap = (b-a)/n
approx_error_trap = (b-a)**3 * abs(f(1) - 2*f(0.5) + f(0)) / (12 * n**2)

print("Approximate Error (Треугольник):", approx_error_rect)
print("Approximate Error (Трапеция):", approx_error_trap)

