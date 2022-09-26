q = input("I = K * i \nНеизвестно: I, K, i (нужное выбрать): ")

if q == "I":
    K = int(input('\nКоличество символов: '))
    i = int(input('\nИнформационный вес символа: '))
    print(f"\nДано:    | Решение:     ")
    print(f"---------+--------------")
    print(f"K = {K}    | I = K * i")
    print(f"i = {i}    | I = {K} * {i}")
    print(f"---------+--------------")
    print(f"Найти: I | Ответ: {K*i}")

elif q == "K":
    I = int(input('\nИнформационный объём: '))
    i = int(input('\nИнформационный вес символа: '))
    print(f"\nДано:    | Решение:     ")
    print(f"---------+--------------")
    print(f"I = {I}    | K = I / i")
    print(f"i = {i}    | K = {I} / {i}")
    print(f"---------+--------------")
    print(f"Найти: K | Ответ: {I/i if (I/i)%1 != 0 else int(I/i)}")

elif q == "i":
    I = int(input('\nИнформационный объём: '))
    K = int(input('\nКоличество символов: '))
    print(f"\nДано:    | Решение:     ")
    print(f"---------+--------------")
    print(f"I = {I}    | i = I / K")
    print(f"K = {K}    | i = {I} / {K}")
    print(f"---------+--------------")
    print(f"Найти: i | Ответ: {I/K if (I/K)%1 != 0 else int(I/K)}")

else:
    print("Неверные входные данные")

input()
