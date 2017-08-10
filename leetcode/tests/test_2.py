'''
Usage:
    test addTwoNumbers_2.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from addTwoNumbers_2 import ListNode
from addTwoNumbers_2 import Solution
from addTwoNumbers_2 import Solution2


def solution(L1, L2):
    l1 = ListNode(0)
    p1 = l1
    l2 = ListNode(0)
    p2 = l2
    for i in xrange(len(L1)):
        tmp = ListNode(0)
        tmp.val = L1[i]
        p1.next = tmp
        p1 = tmp
    for i in xrange(len(L2)):
        tmp = ListNode(0)
        tmp.val = L2[i]
        p2.next = tmp
        p2 = tmp

    cs = Solution()
    l3 = cs.addTwoNumbers(l1.next, l2.next)
    tmpL = []
    while l3:
        tmpL.append(l3.val)
        l3 = l3.next
    return tmpL

def solution2(L1, L2):
    l1 = ListNode(0)
    p1 = l1
    l2 = ListNode(0)
    p2 = l2
    for i in xrange(len(L1)):
        tmp = ListNode(0)
        tmp.val = L1[i]
        p1.next = tmp
        p1 = tmp
    for i in xrange(len(L2)):
        tmp = ListNode(0)
        tmp.val = L2[i]
        p2.next = tmp
        p2 = tmp

    cs = Solution2()
    l3 = cs.addTwoNumbers(l1.next, l2.next)
    tmpL = []
    while l3:
        tmpL.append(l3.val)
        l3 = l3.next
    return tmpL

test_data = [
    ([3, 7],    [9, 2],    [2, 0, 1]),
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([5],       [5],       [0, 1]),
    ([9, 8],    [1],       [0, 9]),
    ([9, 9],    [1],       [0, 0, 1]),
]


@pytest.mark.parametrize("L1,L2,expected", test_data)
def test_solution(L1, L2, expected):
    assert solution(L1, L2) == expected
    assert solution2(L1, L2) == expected
