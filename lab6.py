import functools

x_value = [1.375, 1.380, 1.385, 1.390, 1.395, 1.400]
y_value = [5.04192, 5.17744, 5.32016, 5.47069, 5.62968, 5.79788]

x = 1.3934

def get_index(x):
    for i in range(len(x_value) - 1):
        if x_value[i] < x < x_value[i+1]:
            return i + 1

def get_measurement(n, x):
    difference = [x_value[i + 1] - x_value[i] for i in range(n)]
    measure = functools.reduce(lambda a, b : a * b, difference)
    p = []
    res = 0
    for i in range(n):
        for j in range(n):
            if j != i:
                p.append((x - x_value[j]) / (x_value[i] - x_value[j]))
        cur = functools.reduce(lambda a, b : a * b, p) * y_value[i]
        res += cur
    return res

print(f"L(x={x})= {get_measurement(get_index(x), x)}")
