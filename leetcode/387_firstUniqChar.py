'''
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
    Note: You may assume the string contain only lowercase letters.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index = [s.index(t) for t in letters if s.count(t) == 1]
        return min(index) if len(index) > 0 else -1

if __name__ == '__main__':
    cs = Solution()
    s = "lovecode"
    print s
    print cs.firstUniqChar(s)

