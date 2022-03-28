
def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y




if __name__ == "__main__":
    n1 = int(input("enter n1 : "))
    n2 = int(input("enter n2 : "))

    r1 = add(n1,n2)
    r2 = sub(n1, n2)
    r3 = mul(n1, n2)
    r4 = div(n1, n2)

    print(r1)
    print(r2)
    print(r3)
    print(r4)