import math
def f12():


    def text():
        print('I = K * i')
        print('N = 2^i')
        ans = input('Необходимо найти I, K, i, N: ')

        match ans:
            case 'I':
                K = input('K = ')
                i = input('i = ')
                print(f'I = {K * i}')

            case 'K':
                I = input('I = ')
                i = input('i = ')
                print(f'K = {I / i}')
            case 'i':
                N = input('N = ')
                if N == '':
                    I = input('I = ')
                    K = input('K = ')
                    print(f'i = {I / K}')
                else:
                    print(f'i = {math.log2(N)}')
            case 'N':
                i = input('i = ')
                print(f'N = {2**i}')

    def sound():
        print('V = I * M * t * k')
        ans = input('Необходимо найти V, I, M, t, k: ')

        match ans:
            case 'V':
                I = input('I = ')
                M = input('M = ')
                t = input('t = ')
                k = input('k = ')
                print(f'V = {I * M * t * k}')

            case 'I':
                V = input('V = ')
                M = input('M = ')
                t = input('t = ')
                k = input('k = ')
                print(f'I = {V / (M * t * k)}')

            case 'M':
                V = input('V = ')
                I = input('I = ')
                t = input('t = ')
                k = input('k = ')
                print(f'M = {V / (I * t * k)}')

            case 't':
                V = input('V = ')
                M = input('M = ')
                I = input('I = ')
                k = input('k = ')
                print(f't = {V / (I * M * k)}')

            case 'k':
                V = input('V = ')
                M = input('M = ')
                I = input('I = ')
                t = input('t = ')
                print(f'k = {V / (I * M * t)}')

    def picture():
        print('I = i * X * Y')
        ans = input('Необходимо найти I, i, X, Y: ')

        match ans:
            case 'I':
                i = input('i = ')
                X = input('X = ')
                Y = input('Y = ')
                print(f'I = {i * X * Y}')

            case 'i':
                I = input('I = ')
                X = input('X = ')
                Y = input('Y = ')
                print(f'i = {I / (X * Y)}')

            case 'X':
                I = input('I = ')
                i = input('i = ')
                Y = input('Y = ')
                print(f'i = {I / (i * Y)}')

            case 'Y':
                I = input('I = ')
                i = input('i = ')
                X = input('X = ')
                print(f'i = {I / (i * X)}')


    A = input('Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация')
    match A:
        case '1':
            text()
        case '2':
            sound()
        case '3':
            picture()
