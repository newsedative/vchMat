import math

def f(x):
  return math.tan(3*x**2 + 1) / (x + 1)

def simpsons_rule(a, b, n):
  h = (b - a) / n
  x = [a + i * h for i in range(n + 1)]
  y = [f(xi) for xi in x]
  integral = h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]) + y[-1])
  return integral


def find_n(a, b, tolerance):
    n = 2
    while True:
        integral = simpsons_rule(a, b, n)
        if n > 10000:
            return "Cannot reach the specified tolerance."
        if n > 2:
            integral_prev = simpsons_rule(a,b, n-2)
            if abs(integral - integral_prev) < tolerance:
                return n
        n += 2

a = 0.5
b = 1.7
tolerance = 0.0001

n = find_n(a, b, tolerance)
if type(n) == str:
    print(n)
else:
    integral = simpsons_rule(a, b, n)
    print(f"Номер интервала (n): {n}")
    print(f"Интеграл: {integral}")


