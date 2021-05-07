import random

answer = random.randint(1, 100)
count = 0
while True:
    count += 1
    number = int(input('请输入：'))
    if number > answer:
        print('太大了！')
    elif number < answer:
        print('太小了！')
    else:
        print('恭喜你猜对了，最后的答案是%d，一共猜了%d次' % (number, count))
        break

if count > 7:
    print('您的智商余额不足，请及时充值！')