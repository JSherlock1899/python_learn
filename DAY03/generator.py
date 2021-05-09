gen = (x for x in range(1,40000000000))

print(next(gen))
print(next(gen))
print(next(gen))


# for x in gen:
#     print(x)

print('------------------------------')

# def fib(n):
#     a, b, = 0, 1
#     count = 0
#     res = []
#
#     while True:
#         if(count >= n):
#             break
#         count += 1
#         a, b = b, a + b
#         res.append(a)
#     return res

def fib(n):
    a, b, = 0, 1
    count = 0

    while True:
        if(count >= n):
            break
        count += 1
        a, b = b, a + b
        yield a

gen = fib(100000000000)

for x in gen:
    print(x)
