a = lambda x: x * 2 + 1
def b(b, x):
    # return b(x + a(x))
    return b(1)
x = 3
c= b(a, x)
print(c)