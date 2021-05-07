# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:08:57 2020

@author: playjo
@mail: gww@139.com


"""

import random

while True:
    num='0123456789'
    num4=random.sample(num,4)
    #print(num4)
    num4_str=''.join(num4)
    #print(num4_str)
    print('''
        猜数字（又称 Bulls and Cows ）
        是一种古老的的密码破译类益智类小游戏，起源于20世纪中期。
        
        游戏规则：
        每猜一个数字，电脑根据这个数字给出几A几B，
        其中A前面的数字表示位置正确的数的个数，而B前的数字表示数字正确而位置不对的数的个数。
        如正确答案为 5234，而猜的人猜 5346，则是 1A2B，其中有一个5的位置对了，记为1A，
        而3和4这两个数字对了，而位置没对，因此记为 2B，合起来就是 1A2B。
        游戏设有猜测次数的上限是8次。
        根据计算机测算，如果采用严谨的猜测策略，任何数字最多7次就可猜出（即达到 4A0B）。
        
        试试你的能力吧！！！''')
    d=8
    while d>0:
        print('\n你一共有8次机会，现在还剩{}次，请仔细考虑'.format(d))
        gue=input('请输入四位不同的数字，猜猜看：')
        d=d-1
        if len(gue)==4:
            a,b,y=0,0,0
            for c in gue:
                if c==num4_str[y]:
                    a=a+1
                    
                else:
                    if c in num4_str:
                        b=b+1
                y=y+1
            print('你猜中的是{}A{}B'.format(a,b))
            
            if a==4:
                print('\n你太厉害了，总共猜了{}次，已经胜利过关！(๑•̀ㅂ•́)و✧'.format(8-d))
                break
        else:
            print('位数不正确，请重新输入。')
            d=d+1
    if d==0 and a!=4:
        print('\n你已经没有机会了o(╥﹏╥)o\n正确的答案是{}'.format(num4_str))
    game=input('\n是否再来一局？1继续，其它退出：')
    if game=='1':
        continue
    else:
        break
print('\n\n游戏结束！！ヾ(￣▽￣)Bye~Bye~')