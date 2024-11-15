x_value = [0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26]
y_value = [4.4817, 4.9530, 5.4739, 6.0496, 6.6859, 7.3891, 8.1662, 9.0250, 9.9742, 11.0232, 12.1825, 13.4637]
x1 = 0.1732
x2 = 0.2444

dy = [y_value[i + 1] - y_value[i] for i in range(len(y_value) - 1)]
dy1 = [dy[i + 1] - dy[i] for i in range(len(dy) - 1)]
dy2 = [dy1[i + 1] - dy1[i] for i in range(len(dy1) - 1)]
dy3 = [dy2[i + 1] - dy2[i] for i in range(len(dy2) - 1)]
dy4 = [dy3[i + 1] - dy3[i] for i in range(len(dy3) - 1)]
dy5 = [dy4[i + 1] - dy4[i] for i in range(len(dy4) - 1)]
dy6 = [dy5[i + 1] - dy5[i] for i in range(len(dy5) - 1)]
dy7 = [dy6[i + 1] - dy6[i] for i in range(len(dy6) - 1)]
dy8 = [dy7[i + 1] - dy7[i] for i in range(len(dy7) - 1)]
dy9 = [dy8[i + 1] - dy8[i] for i in range(len(dy8) - 1)]
dy10 = [dy9[i + 1] - dy9[i] for i in range(len(dy9) - 1)]

sp = [dy, dy1, dy2, dy3, dy4, dy5, dy6, dy7, dy8, dy9, dy10]

for i in range(len(x_value)):
    print(f"{x_value[i]:.3f} {y_value[i]:.3f} {dy1[i] if i < len(dy1) else 0:.6f}  {dy2[i] if i < len(dy2) else 0:.6f}"
            f"  {dy3[i] if i < len(dy3) else 0:.6f}  {dy4[i] if i < len(dy4) else 0:.6f}  {dy5[i] if i < len(dy5) else 0:.6f}"
            f"  {dy6[i] if i < len(dy6) else 0:.6f}   {dy7[i] if i < len(dy7) else 0:.6f}   "
            f"  {dy8[i] if i < len(dy8) else 0:.6f}   {dy9[i] if i < len(dy9) else 0:.6f}   {dy10[i] if i < len(dy10) else 0:.6f} ")


def get_index(x):
    for i in range(len(x_value) - 1):
        if x_value[i] < x < x_value[i+1]:
            return i


def result_func(x):
    index = get_index(x)
    q = (x - x_value[0]) / 0.005
    if index > (len(x_value) / 2):
        result = y_value[index] + q * dy[index] + ((q * (q - 1))/2)*pow(dy[index], 2) + ((q * (q - 1) * (q - 2))/2 * 3)*pow(dy[index], 3)
    else:
        index += 1
        result = y_value[index] + q * sp[index - 1][index] + (q * (q + 1)/2)*pow(sp[index - 2][index], 2) + (q * (q + 1) * (q + 2) / 2*3)*pow(sp[index - 3][index], 3)

    return result


print(result_func(x1))
