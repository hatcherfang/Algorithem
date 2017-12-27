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
        int closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i <= len-2; i ++){
            if (i > 0 && i <= len-2 && nums[i] == nums[i-1]){
                continue;
            }
            int left = i;
            int mid = i + 1;
            int right = len-1;
            while (mid < right){
                int total = nums[left] + nums[mid] + nums[right];
                if (total - target < 0){
                    mid ++;
                    if (Math.abs(total-target) < Math.abs(closest-target)){
                        closest = total;
                        System.out.format("nums[left]:%d, nums[mid]:%d, nums[right]:%d\n",
                                nums[left], nums[mid], nums[right]);
                    }
                }
                else if (total - target > 0){
                    right --;
                    if (Math.abs(total-target) < Math.abs(closest-target)){
                        closest = total;
                        System.out.format("nums[left]:%d, nums[mid]:%d, nums[right]:%d\n",
                                nums[left], nums[mid], nums[right]);
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
