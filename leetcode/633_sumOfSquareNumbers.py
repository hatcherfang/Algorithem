'''
633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two
integers a and b such that pow(a, 2) + pow(b, 2) = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            mid = (left + right)/2
            if mid**2 > x:
                right = mid-1
            elif mid**2 < x:
                left = mid+1
            else:
                return mid
        return left-1

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            mid = (left + right) / 2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if self.isPerfectSquare(c):
            return True
        left = 1
        right = self.mySqrt(c) + 1
        while left <= right:
            if pow(left, 2) + pow(right, 2) < c:
                left = left + 1
            elif pow(left, 2) + pow(right, 2) > c:
                right = right - 1
            else:
                return True
        return False

if __name__ == '__main__':
    c = 2
    c = 999999999
    cs = Solution()
    print cs.judgeSquareSum(c)
