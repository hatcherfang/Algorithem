'''
Usage:
    test longestSubstrLen_3.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from longestSubstrLen_3 import Solution


test_data = [
    ("abcabcbb", 3),
    ('bbbbbb', 1),
    ('c', 1),
    ('aab', 2)
]


@pytest.mark.parametrize("strings,expected", test_data)
def test_solution(strings, expected):
    cs = Solution()
    assert cs.lengthOfLongestSubstring(strings) == expected
