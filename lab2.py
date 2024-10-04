x1 = 0.19
x2 = 0.97
x3 = -0.14

print('n x1    x2    x3')
flag = True
i = 0
while flag:
    print(i, ("%.4f" % x1), ("%.4f" % x2), ("%.4f" % x3))
    a = x1
    b = x2
    c = x3
    x1 = 0.24 * round(x1, 4) - 0.05 * round(x2, 4) - 0.24 * round(x3, 4) + 0.19
    x2 = -0.22 * round(x1, 4) + 0.09 * round(x2, 4) - 0.44 * round(x3, 4) + 0.97
    x3 = 0.13 * round(x1, 4) - 0.02 * round(x2, 4) + 0.42 * round(x3, 4) - 0.14
    if abs(a - x1) < 0.0001 and abs(b - x2) < 0.0001 and abs(c - x3) < 0.0001:
        flag = False

    i += 1


print(i, ("%.4f" % x1), ("%.4f" % x2), ("%.4f" % x3))



x1 = 0.245
x2 = -0.215
x3 = -0.455

print('n x1    x2    x3')
flag = True
i = 0
while flag:
    print(i, ("%.4f" % x1), ("%.4f" % x2), ("%.4f" % x3))
    a = x1
    b = x2
    c = x3
    x1 = 0.495 * round(x1, 4) - 0.06 * round(x2, 4) - 0.315 * round(x3, 4) + 0.245
    x2 = -0.005 * round(x1, 4) + 0.865 * round(x2, 4) + 0.065 * round(x3, 4) - 0.215
    x3 = -0.095 * round(x1, 4) + 0.42 * round(x2, 4) - 0.185 * round(x3, 4) - 0.455
    if abs(a - x1) < 0.0001 and abs(b - x2) < 0.0001 and abs(c - x3) < 0.0001:
        flag = False

    i += 1


print(i - 1, ("%.3f" % x1), ("%.3f" % x2), ("%.3f" % x3))
