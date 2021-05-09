def max2(list):
    m1, m2 = (list[0], list[1]) if list[0] > list[1] else (list[1], list[0])

    for index in range(2, len(list)):
        if list[index] > m1:
            m2 = m1
            m1 = list[index]
        elif list[index] > m2:
            m2 = list[index]
    return m1,m2

if __name__ == '__main__':
    print(max2([2,65,6,1,6,333332,67,214,61314,2,1,0]))
