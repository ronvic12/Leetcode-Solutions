class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Point to the first unique K element
        # Compare next K element to the first unique element
        # if pointed element is same as next element, then delete the next K element. Otherwise move to the next K element.

        j = 1
    # this allows to use in range from 1 to input size
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]: 
                nums[j] = nums[i]
                j += 1 
        return j
         
