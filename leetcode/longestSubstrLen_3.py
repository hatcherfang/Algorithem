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
        index = 0
        maxLen = -1
        subList = []
        for i, sub in enumerate(s):
            if sub not in subList:
                subList.append(sub)
            else:
                if len(subList) > maxLen:
                    maxLen = len(subList)
                    index = i - maxLen
                subList = subList[subList.index(sub)+1:]
                subList.append(sub)
        if maxLen == -1:
            maxLen = len(subList)
        elif maxLen < len(subList):
            maxLen = len(subList)
            index = len(s) - len(subList)
        return maxLen

if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = 'c'
    s = 'aab'
    cs = Solution()
    r = cs.lengthOfLongestSubstring(s)
    print r
    print s[r[1]:r[1]+r[0]]

