public class Solution {
    public int RemoveElement(int[] nums, int val) {
        // track the K element
        int k = 0;

        for(int i = 0; i < nums.Length; i++)
        {
            if(nums[i] != val)
            {
                // Keep looking for value to be removed
                nums[k] = nums[i];
                k++;
            }

        }
        return k;
    }
}