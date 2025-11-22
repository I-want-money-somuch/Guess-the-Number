#数字炸弹
import pygame
import random
print('1-100随机数(你有十次机会)')
c=0
num= int(random.randint(1, 100))
while True:
    if c == 10:
        print('你没机会了')
        #str()的作用是把纯数字(可以进行运算的数字)转换成字符串.
        #int()的作用则是把字符串形式的数字转换成纯数字(可以进行运算的数字).
        d = '答案是' + str(num)
        print(d)
        break
    a = int(input())
    if a == num:
        print('你赢了')
        break
    else:
        if a >= num:
            print('太大了')
            c += 1
        else:
            print('太小了')
            c += 1

