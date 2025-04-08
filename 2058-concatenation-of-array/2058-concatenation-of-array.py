class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        

        n = len(nums)
        double_n = n * 2
        ans = [0] * (double_n)


        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans

      