'''
7. Reverse Integer


Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
    The input is assumed to be a 32-bit signed integer. Your function should
    return 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        # thinking: use flag to save the sign
        # rnum should be less than 2**31
        flag = cmp(x, 0)
        x = x*flag
        rnum = 0
        while x:
            num = x % 10
            x = x / 10
            if x > 0:
                rnum = (rnum + num)*10
            else:
                rnum = rnum + num
        return flag*rnum*(rnum < 2**31)


class Solution2(object):
    def reverse(self, x):
        flag = cmp(x, 0)
        # reverse
        x = int(repr(x*flag)[::-1])
        return flag*x*(x < 2**31)

if __name__ == '__main__':
    s = Solution()
    cs2 = Solution2()
    x = -123456789
    print x
    print s.reverse(x)
    print cs2.reverse(x)
