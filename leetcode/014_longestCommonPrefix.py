'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array
of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        row_len = len(strs)
        i = 0  # row num
        j = 0  # col num
        if row_len < 2:
            return strs[0] if len(strs) else ""
        while j < len(strs[i]) and j < len(strs[i+1]):
            while i + 1 < row_len:
                if j >= len(strs[i]):
                    return strs[i]
                elif j >= len(strs[i+1]):
                    return strs[i+1]
                elif strs[i][j] == strs[i+1][j]:
                    i = i + 1
                else:
                    break
            if i + 1 < row_len:
                if j > 0:
                    return strs[0][0:j]
                else:
                    return ""
            else:
                j = j + 1
                i = 0

        if j >= len(strs[i]):
            return strs[i]
        elif j >= len(strs[i+1]):
            return strs[i+1]

if __name__ == "__main__":
    strs = ["abab", "aba", "abc"]
    strs = ["abab", "", "abc"]
    strs = ["abab", "abc", ""]
    cs = Solution()
    print cs.longestCommonPrefix(strs)
