A=int(input('Введите число'))
B=int(input('Введите число меньше первого'))
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i, end=' ')