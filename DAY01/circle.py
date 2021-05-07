import math

radius = float(input('请输入圆的半径：'))
c = 2 * math.pi * radius
s = math.pi * radius * radius
print('周长为%.2f，面积为%.2f' % (c, s))
