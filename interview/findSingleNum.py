# -*- coding: utf8 -*-
'''
找出单一数
 输入一组数字，该组数字有以下几个特性：
该组数除了1个数，其他数都是成对出现
成对或者单个存在的数字和相邻的数都不相等
数字不是有序的
要求将数组中唯一单次出现的数字输出。

输入描述:
输入一组数字，以空格为分割
输出描述:
输出找到的单个数字
'''


class solution:
    def search_single(self):
        L = list(map(int, input().split(" ")))
        if L == []:
            return None
        item = L[0]
        for i in range(1, len(L)):
            item = item ^ L[i]
        return item

    def search_single2(self):
        # s = input()
        s = '22 22 33 33 2'
        num = s.split(' ')
        num = list(map(int, num))
        for i in range(0, len(num)-1, 2):
            if i == len(num)-1:
                print(num[-1])
                break
            if num[i] != -num[i+1]:
                print(num[i])
                break  


s = '22 22 33 33 2'
S = solution()
print(S.search_single())
# print(S.search_single2())
