/*
 * 148. Sort List
 *
 * Sort a linked list in O(n log n) time using constant space complexity.
 * */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
     public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // l1 and l2 with head node
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        ListNode l3 = new ListNode(0);
        ListNode w = l3;
        ListNode p = l1;
        ListNode q = l2;
        while (p != null && q != null){
                if (p.val > q.val){
                    w.next = q;
                    q = q.next;
                }
                else {
                    w.next = p;
                    p = p.next;
                }
            w = w.next;
        }
        if (p != null){
            w.next = p;
        }
        if (q != null){
            w.next = q;
        }
        return l3.next;
    }
    public ListNode sortList(ListNode head) {
        // cut the list into two halves and then sort them recursivly
        if (head == null || head.next == null){
            return head;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (slow != null && fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode p = slow.next;
        slow.next = null;
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(p);
        return mergeTwoLists(l1, l2);
    }
}
