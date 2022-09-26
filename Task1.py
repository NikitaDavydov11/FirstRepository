p = int(input("p = "))
Np = int(input(f"N{p} = "))

K = 1
N10 = 0

while Np != 0:
    N10 = N10 + Np % 10 * K
    K = K * p
    Np = Np//10

print(f"N10 = {N10}")
