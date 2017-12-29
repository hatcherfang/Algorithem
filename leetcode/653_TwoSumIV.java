/*
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean findTarget(TreeNode root, int k) {
       Map map = new HashMap();
       TreeNode treeNode = root;
       Stack stack = new Stack();
       while (treeNode != null || !stack.empty()){
           if (treeNode != null){
               if (map.containsKey(k-treeNode.val)){
                   return true;
               }
               stack.push(treeNode);
               map.put(treeNode.val, 1);
               treeNode = treeNode.left;
           }
           else {
               treeNode = (TreeNode) stack.pop();
               treeNode = treeNode.right;
           }
       }
       return false; 
    }
}
