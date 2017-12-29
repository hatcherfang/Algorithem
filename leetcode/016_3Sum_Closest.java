/*
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is

closest to a given number, target. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums.length < 3){
            return -1;
        }
        int len = nums.length;
        Arrays.sort(nums);
        int distance = Integer.MAX_VALUE;
        int closest = 0;
        for (int i = 0; i < len-2; i ++){
            if (i > 0 && i < len-2 && nums[i] == nums[i-1]){
                continue;
            }
            int left = i;
            int mid = i + 1;
            int right = len-1;
            while (mid < right){
                int total = nums[left] + nums[mid] + nums[right];
                if (total - target < 0){
                    mid ++;
                    if ((target-total) < distance){
                        distance = target-total;
                        closest = total;                     
                    }
                }
                else if (total - target > 0){
                    right --;
                    if ((total-target) < distance){
                        distance = total-target;
                        closest = total;
                    }
                }
                else {
                    return total;
                }
            }
        }
        return closest;
    } 
}

}
