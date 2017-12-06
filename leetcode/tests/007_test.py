'''
Usage:
    test reverseInteger_7.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from reverseInteger_7 import Solution
from reverseInteger_7 import Solution2


test_data = [
    (-123456789, -987654321),
    (123456789, 987654321),
    (678543, 345876),
    (1378, 8731)
]


@pytest.mark.parametrize("num,expected", test_data)
def test_solution(num, expected):
    cs = Solution()
    assert cs.reverse(num) == expected

    cs2 = Solution2()
    assert cs2.reverse(num) == expected
