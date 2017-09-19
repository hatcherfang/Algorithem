'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''


class Solution(object):
    def isPalindrome(self, substring):
        if not substring:
            return False
        i = 0
        j = len(substring)-1
        while i <= j and substring[i] == substring[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        longestLen = 0
        substring = ""
        for i in range(slen):
            j = i + 1
            for j in range(slen):
                if self.isPalindrome(s[i:j+1]):
                    if j+1-i >= longestLen:
                        longestLen = j+1-i
                        substring = s[i:j+1]
        return substring


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = s[::-1]
        slen = len(s)
        longestLen = 0
        substring = ""
        for i in range(slen):
            j = i + 1
            for j in range(slen):
                if s[i:j+1] in rs and j+1-i >= longestLen and \
                        rs.index(s[i:j+1]) == rs.index(s[i:j+1][::-1]):
                    substring = s[i:j+1]
                    longestLen = j+1-i
        return substring


class Solution3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''dynamic programming'''
        pass

if __name__ == '__main__':
    s = "babad"
    cs = Solution()
    print cs.longestPalindrome(s)
    cs2 = Solution2()
    print cs2.longestPalindrome(s)
