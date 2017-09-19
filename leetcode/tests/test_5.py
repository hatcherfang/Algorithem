'''
Usage:
    test longestPalinSubstr_5.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from longestPalinSubstr_5 import Solution
from longestPalinSubstr_5 import Solution2

test_data = [
    ('abac', 'aba'),
    ('ababc', 'bab'),
    ('abcdabc', 'c'),
    ('abcdcbaabc', 'abcdcba')
]


@pytest.mark.parametrize("s, expected", test_data)
def test_solution(s, expected):
    cs = Solution()
    assert cs.longestPalindrome(s) == expected
    cs2 = Solution2()
    assert cs2.longestPalindrome(s) == expected
