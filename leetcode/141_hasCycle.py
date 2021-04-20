# -*-coding:utf-8 -*-
'''
141. 环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        pre = head
        post = pre.next
        while post and pre and pre != post:
            if not post.next:
                return False
            post = post.next.next
            pre = pre.next
        if post and pre and pre == post:
            return True
        return False

    def createList(self, L, pos):
        if not L:
            return
        i = 0
        pHead = None
        length = len(L)
        # if pos >= length:
        #     return
        pNode = None
        while i < length:
            t = ListNode(L[i])
            if not pHead:
                pHead = t
                p = pHead
            p.next = t
            p = t
            if pos == i:
                pNode = t
            i += 1
        p.next = pNode
        # print('val:%r' % pNode.val)
        return pHead

    def printList(self, pHead):
        if not pHead:
            return
        p = pHead
        # i = 20
        while p:
            print(p.val)
            p = p.next
            # if not i:
            #     break
            # i = i - 1


if __name__ == '__main__':
    cs = Solution()
    L = [1, 2, 3, 4, 5]
    pos = 1
    pHead = cs.createList(L, pos)
    # cs.printList(pHead)
    ret = cs.hasCycle(pHead)
    print(ret)
