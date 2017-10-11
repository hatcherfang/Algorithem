'''
8. String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely
(ie, no given input specs). You are responsible to gather all the input
requirements up front.
'''


class Solution(object):
    def removeFirstEmpty(self, str):
        i = 0
        while i < len(str) and str[i] == ' ':
            i = i + 1
        str = str[i:]
        return str

    def removeFirstZero(self, str):
        i = 0
        while i < len(str) and str[i] == '0':
            i = i + 1
        str = str[i:]
        return str

    def getFirstDigit(self, str):
        i = 0
        while i < len(str) and str[i].isdigit():
            i = i + 1
        return str[:i]

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = self.removeFirstEmpty(str)
        if str[0] in ['-', '+']:
            flag = str[0]
            if len(str) >= 2:
                str = self.removeFirstZero(str[1:])
                digit = self.getFirstDigit(str)
                if digit:
                    if flag == '+':
                        return int(digit) if int(digit) <= 2147483647 else 2147483647
                    else:
                        return int(digit)*(-1) if int(digit)*(-1) >= -2147483648 else -2147483648
                else:
                    return 0
            else:
                return 0
        else:
            str = self.removeFirstZero(str)
            digit = self.getFirstDigit(str)
            if digit:
                return int(digit) if int(digit) <= 2147483647 else 2147483647
            return 0

if __name__ == '__main__':
    cs = Solution()
    # print cs.myAtoi("    010")
    # print cs.myAtoi("  -0012a42")
    # print cs.myAtoi("1")
    # print cs.myAtoi("+-2")
    print cs.myAtoi("+1")
