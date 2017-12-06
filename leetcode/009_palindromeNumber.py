'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
    Could negative integers be palindromes? (ie, -1)

    If you are thinking of converting the integer to string, note the
    restriction of using extra space.

    You could also try reversing an integer. However, if you have solved the
    problem "Reverse Integer", you know that the reversed integer might
    overflow. How would you handle such case?

    There is a more generic way of solving this problem.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        sumA = 0
        tmp = x
        while x:
            sumA = sumA*10 + (x % 10)
            x = x/10
        return sumA == tmp


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        sumA = 0
        while x > sumA:
            sumA = sumA*10 + (x % 10)
            x = x/10
        return x == sumA or x == sumA/10

if __name__ == "__main__":
    x = 121
    x = 1221
    x = 10
    cs = Solution()
    print cs.isPalindrome(x)
    cs2 = Solution2()
    print cs2.isPalindrome(x)
