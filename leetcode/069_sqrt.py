'''
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an
integer, the decimal part will be truncated.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = x / 2
        while left**2 > x:
            left = left/2
        while left**2 < x:
            left = left + 1
        if left**2 > x:
            left = left - 1
        return left


class Solution2(object):
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

if __name__ == '__main__':
    x = 121
    x = 8
    cs = Solution()
    print cs.mySqrt(x)
    cs2 = Solution2()
    print cs2.mySqrt(x)
