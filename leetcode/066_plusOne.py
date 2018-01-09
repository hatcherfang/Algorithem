'''
66. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus
one to the integer.

You may assume the integer do not contain any leading zero, except the number 0
itself.

The digits are stored such that the most significant digit is at the head of the
list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        len1 = len(digits)
        i1 = len1 - 1
        carry = 1
        while carry == 1:
            if i1 >= 0:
                value = digits[i1] + carry
                if value >= 10:
                    carry = 1
                    digits[i1] = value - 10
                    i1 = i1 - 1
                else:
                    digits[i1] = value
                    return digits
            else:
                digits.insert(0, 1)
                break
        return digits

if __name__ == '__main__':
    digits = [9, 9, 9]
    cs = Solution()
    print cs.plusOne(digits)
