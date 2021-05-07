def function01(a=1, b=2, c=3):
    return a + b + c

print(function01(3))

def function02(*args):
    total = 0
    for x in args:
        total += x
    return total

print(function02(2,5,7,1,2))


