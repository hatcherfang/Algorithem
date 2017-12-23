class Solution {
    public void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    public void sortColors(int[] nums) {
        // put red at front and blue at back
        // the white will be at the middle in the end.
        if (nums == null || nums.length == 0)
            return;
        int back = nums.length - 1;
        int front = 0;
        int r = 0;
        int red = 0;
        int blue = 2;
        while(r <= back){
            if (nums[r] == red){
                swap(nums, r, front);
                r ++;
                front ++;
            }
            else if (nums[r] == blue){
                swap(nums, r, back);
                back--;
            }
            else {
                r ++;
            }
        }
    }
    public void sortColors2(int[] nums) {
        int[] tmp = new int[3];
        int len = nums.length;
        for (int i = 0; i < len; i ++) {
            tmp[nums[i]] ++;
        }
        int k = 0;
        for (int i = 0; i < 3; i ++) {
            for (int j = 0; j < tmp[i]; j ++){
                nums[k++] = i ;
            }
        }
    }
}
