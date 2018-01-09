'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        carry = 0
        ia = len(a) - 1
        ib = len(b) - 1
        c = ""
        while ia >= 0 or ib >= 0 or carry == 1:
            v1 = 0
            v2 = 0
            if ia >= 0:
                v1 = int(a[ia])
                ia = ia - 1
            if ib >= 0:
                v2 = int(b[ib])
                ib = ib - 1
            value = v1 + v2 + carry
            if value >= 2:
                carry = 1
                c = str(value - 2) + c
            else:
                carry = 0
                c = str(value) + c
        return c

if __name__ == "__main__":
    a = "111"
    b = "1"
    cs = Solution()
    print cs.addBinary(a, b)
