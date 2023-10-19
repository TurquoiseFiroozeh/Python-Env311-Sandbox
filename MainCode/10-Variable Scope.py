import builtins
"LEGB, Local, Enclosing, Global, Built-in"


x = 'global x'


def test():
    "sho the vaiable"
    y = 'local y'
    print(y)
    print(x)


test()
print(x)

print("\n")


def test2():
    x = 'local x'
    print(x)


test2()
print(x)

print("\n")


def test3():
    global x
    x = 'global local x'
    print(x)


test3()
print(x)

print("\n")


def test4():
    global z
    z = 'global local z'
    print(z)


test4()
print(z)

print("\n")


def test5(z):
    x = 'local x'
    print(z)


test5('local z')

print("\n")
m = min([5, 1, 4, 2, 3])
print(m)

print("\n")

print(dir(builtins))


def min():
    pass


# m = min([5, 4, 2, 6])
# print(m)

print("\n")


def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x)
    inner()
    print(x)


outer()

print("\n")


def outer2():
    x = "outer x"

    def inner2():
        nonlocal x
        x = "inner x"
        print(x)
    inner2()
    print(x)


outer2()

print("\n")


def outer3():
    x = "outer x"

    def inner3():
        x = "inner x"
        print(x)
    inner3()
    print(x)


outer3()
print(x)
