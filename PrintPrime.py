def IsDivisible(m, n):
    if m % n == 0:
        return 1
    else:
        return 0


def IsPrime(m):
    f = 1
    for n in range(2, int(m ** 0.5) + 1):
        if IsDivisible(m, n) == 0:
            f = 0
            break
        else:
            f = 1
    if f == 0:
        # print("N")
        return 0
    else:
        # print("Y")
        return 1


def PrintPrime(x):
    for z in range(x):
        if IsPrime(z) == 1:
            print(z)


PrintPrime(100)
