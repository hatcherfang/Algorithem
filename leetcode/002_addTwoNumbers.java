/*
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        ListNode l3 = new ListNode(0);
        l3.next = null;
        ListNode p = l3;
        int carry = 0, value = 0;
        while (l1 != null || l2 !=null || carry > 0){
            value = ((l1 != null) ? l1.val : 0) + ((l2 != null) ? l2.val : 0) + carry;
            if (value >= 10){
               carry = 1;
               value = value - 10;
            }
            else {
               carry = 0;
            }
            ListNode tmp = new ListNode(value);
            p.next = tmp;
            p = tmp;
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        return l3.next;
    }
}

