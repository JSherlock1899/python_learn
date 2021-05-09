set1 = {1, 2, 3, 3, 3, 2}

print(set1)


set2 = {num ** 2 for num in range(0,100) if num % 10 == 0}

set2.update([11,12])
set2.discard(0)

print(set2)

print(set2.pop())