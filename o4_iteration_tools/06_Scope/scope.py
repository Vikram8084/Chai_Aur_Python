username = "chaiaurcode"

def fun():
    username ="chai"
    print(username)

print(username)
fun()


x = 99

# def func2(y):
#     z = x + y
#     return z

# result =func2(1)
# print(result)


# def func3():
#     x = 88


# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))