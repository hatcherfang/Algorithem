'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # index = 0
        maxLen = 0
        subString = ""
        for i, sub in enumerate(s):
            if sub not in subString:
                subString = subString + sub
            else:
                if len(subString) > maxLen:
                    maxLen = len(subString)
                    # index = i - maxLen
                subString = subString[subString.index(sub)+1:]
                subString = subString + sub
        if maxLen < len(subString):
            maxLen = len(subString)
            # index = len(s) - len(subList)
        return maxLen


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        length = len(s)
        tmp_dict = {}
        maxLen = 0
        for index in xrange(length):
            if s[index] in tmp_dict and start <= tmp_dict[s[index]]:
                start = tmp_dict[s[index]] + 1
            else:
                maxLen = max(maxLen, index-start+1)
            tmp_dict[s[index]] = index
        return maxLen


if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = 'c'
    # s = 'aab'
    s = "pwwkew"
    # s = 'pw'
    cs = Solution2()
    r = cs.lengthOfLongestSubstring(s)
    print r
    print s[r[1]:r[1]+r[0]]
