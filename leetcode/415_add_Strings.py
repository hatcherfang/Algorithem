'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to
integer directly.
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1:
            return num2
        if not num2:
            return num1
        len1 = len(num1)
        len2 = len(num2)
        i1 = len1 - 1
        i2 = len2 - 1
        carry = 0
        value = 0
        num3 = ""
        while i1 >= 0 or i2 >= 0 or carry == 1:
            v1 = 0
            v2 = 0
            if i1 >= 0:
                v1 = int(num1[i1])
                i1 = i1 - 1
            if i2 >= 0:
                v2 = int(num2[i2])
                i2 = i2 - 1
            value = v1 + v2 + carry
            if value >= 10:
                carry = 1
                value = value % 10
            else:
                carry = 0
            num3 = str(value) + num3
        return num3
if __name__ == '__main__':
    num1 = "1234"
    num2 = "5678"
    cs = Solution()
    print cs.addStrings(num1, num2)
