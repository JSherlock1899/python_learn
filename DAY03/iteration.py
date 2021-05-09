class IT(object):

    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.counter > 2):
            raise StopIteration()
        self.counter += 1
        return self.counter


obj1 = IT()

# v1 = obj1.__next__()
#
# v2 = obj1.__next__()
#
# v3 = obj1.__next__()
#
# v4 = obj1.__next__()
#
# print(v1)
# print(v2)
# print(v3)
# print(v4)

for item in obj1:
    # 返回的是next的返回值
    print(item)
