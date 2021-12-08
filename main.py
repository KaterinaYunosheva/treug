import math

print("Введите количество чисел в массиве: ")
kol_ch = int(input())
x = [i for i in range(kol_ch)]

x.sort(reverse=True) # в порядке убывания
#print(x)
S = -1
maxS = -1
for i in range(2, kol_ch):
 if ((x[i] < x[i - 2] + x[i - 1]) and (x[i] + x[i - 2] > x[i - 1]) and (x[i-2] < x[i] + x[i - 1])):
    p = (x[i] + x[i - 1] + x[i - 2]) / 2
    S = math.sqrt(p * (p - x[i]) * (p - x[i - 1]) * (p - x[i - 2]))
    # maxS = max(maxS, S)
    if maxS < S:
        maxS = S
        a=x[i-2]
        b=x[i-1]
        c=x[i]

print("Максимальная площадь треугольника =", maxS, "( стороны треугольника :", a, b, c,")" )