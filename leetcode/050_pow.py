'''
50. Pow(x, n)

Implement pow(x, n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not x:
            return 1
        if n == 0:
            return 1
        N = abs(n)
        result = x
        odd_result = 1
        while N > 1:
            if N%2:
                # N is odd number
                odd_result *= result
                N = N - 1
            else:
                result *= result
                N = N/2
        result *= odd_result
        if n < 0:
            result = 1.0/result
        return result

if __name__ == '__main__':
    x = 2
    n = 10
    cs = Solution()
    print cs.myPow(x, n)
