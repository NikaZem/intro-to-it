a, b, c = flat(input()), float(input()), float(input())
if a == 0 and b == 0 and c == 0:
    print("а где коэффициенты")
elif a == 0:
    print("Это не квадратное уравнение")
else:
    D = b**2 - (4 * a * c)
    if D < 0:
        print("Нет решений")
    if D == 0:
        print(f'x = {-b//(2 * a)}')
    if D > 0:
        print(f'x1 = {(-b + (D**0.5))//(2 * a)} x2 = {(-b - (D**0.5))//(2 * a)}')
