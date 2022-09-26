p = int(input("p = "))
print(f"{p}-ичная таблица умножения \n")

X = 1
Y = 1
for X in range(1, p):
    for Y in range(1, p):
        Z = X*Y // p * 10 + X*Y % p
        print(Z, end=" ")
    print()
