/*
 * 23. Merge k Sorted Lists
 *
 * Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
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
    
    public ListNode recursiveMerge(ListNode[] lists, int left, int right){
        if (left >= right)
            return lists[left];
        int mid = (left+right)/2;
        ListNode list1 = recursiveMerge(lists, left, mid);
        ListNode list2 = recursiveMerge(lists, mid+1, right);
        return mergeTwoLists(list1, list2);
    }
     public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0){
            return null;
        }
        return recursiveMerge(lists, 0, lists.length-1);
    }
}
