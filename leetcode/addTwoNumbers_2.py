'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        flag = 0
        p1 = l1
        p2 = l2
        H = ListNode(0)
        p3 = H
        while p1 and p2:
            tmp = ListNode(0)
            tmp.val = (p1.val + p2.val) % 10 + flag
            flag = 0
            if tmp.val/10 >= 1:
                tmp.val = tmp.val % 10
                flag = 1
            flag = flag + (p1.val + p2.val)/10
            p3.next = tmp
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            tmp = ListNode(0)
            tmp.val = p1.val + flag
            flag = 0
            if tmp.val/10 >= 1:
                tmp.val = tmp.val % 10
                flag = 1
            flag = flag + p1.val/10
            p1 = p1.next
            p3.next = tmp
            p3 = p3.next
        while p2:
            tmp = ListNode(0)
            tmp.val = p2.val + flag
            flag = 0
            if tmp.val/10 >= 1:
                tmp.val = tmp.val % 10
                flag = 1
            flag = flag + p2.val/10
            p2 = p2.next
            p3.next = tmp
            p3 = p3.next
        if flag > 0:
            tmp = ListNode(0)
            tmp.val = flag
            p3.next = tmp
            p3 = tmp
            flag = 0
        return H.next


class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
