class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        len1 = len(haystack)
        len2 = len(needle)
        if len1 < len2:
            return -1
        for i in range(len1-len2+1):
            if haystack[i: i+len2] == needle:
                return i
        return -1


if __name__ == "__main__":
    cs = Solution()
    # haystack = "abcabd"
    # needle = "abd"
    # haystack = "hello"
    # needle = "ll"
    haystack = "mississippi"
    needle = "issip"
    needle = "pi"
    print cs.strStr(haystack, needle)
