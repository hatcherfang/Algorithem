'''
Usage:
    test climbStairs_70.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from climbStairs_70 import Solution


test_data = [
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13),
    (7, 21)
]


@pytest.mark.parametrize("num,expected", test_data)
def test_solution(num, expected):
    cs = Solution()
    assert cs.climbStairs(num) == expected
