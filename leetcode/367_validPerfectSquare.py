'''
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a
perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
'''


class Solution(object):
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

if __name__ == '__main__':
    num = 88
    cs = Solution()
    print cs.isPerfectSquare(num)
