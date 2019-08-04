global a

a = 5

def f1(a, b):
    return a + b

def f2(c):
    f=c+a
    print(f)

print(f1(2,2))
print(f2(4))