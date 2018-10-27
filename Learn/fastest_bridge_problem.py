# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-09-22 10:43:54
# @Last Modified by:   何睿
# @Last Modified time: 2018-09-22 12:02:01

import random

'''
    甲；乙；丙；丁四个人过桥，分别需要 1，2，5，10 分钟。因为天黑，必须借助手电筒过桥，
    可是总共只有一个手电筒，并且桥的载重能力有限，只能承受两个人的重量也就是说每次最多
    过两个人，怎样才能做到用最短的时间让他们全部过桥，最短需要多少分钟。
    给出方法。编程实现寻找 方法的过程。 
    返回说明:
        ([(1, 2), 1, (5, 10), 2, (1, 2)], 17)
        1,2过桥，1返回，把电筒给5，10，他们过桥，然后已经在桥另一边的2拿着手电筒过桥，
        最后1，2同时过桥，总时间需要17分钟
'''


def bridge(minutes):
    # 人数
    num = len(minutes)
    if num <= 2:
        return [tuple(minutes)], sum(minutes)
    else:
        # 需要的总时间
        times = 0
        result = []
        # 判读是奇数个人还是偶数个人
        is_even = False if num % 2 else True
        i = 2 if is_even else 3
        s_lst = sorted(minutes)
        while i < num:
            if 2*s_lst[1] >= s_lst[0]+s_lst[i]:
                temp = [(s_lst[0], s_lst[i]), (s_lst[0]),
                        (s_lst[0], s_lst[i+1]), (s_lst[0])]
                result.extend(temp)
                times += sum([2*s_lst[0], s_lst[i], s_lst[i+1]])
                del temp
            else:
                temp = [(s_lst[0], s_lst[1]), (s_lst[0]),
                        (s_lst[i], s_lst[i+1]), (s_lst[1])]
                times += sum([2*s_lst[1], s_lst[0], s_lst[i+1]])
                result.extend(temp)
                del temp
            i += 2
        if is_even:
            result.append((s_lst[0], s_lst[1]))
            times += s_lst[1]
        else:
            temp = [(s_lst[0], s_lst[1]), (s_lst[0]), (s_lst[0], s_lst[2])]
            times += sum([s_lst[1], s_lst[2]])
            result.extend(temp)
        return result, times


if __name__ == "__main__":
    minutes=[1,2,5,10]
    # minutes = random.sample(range(1, 100), 10)
    res = bridge(minutes)
    print(res)