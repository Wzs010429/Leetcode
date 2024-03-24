# leetcode 1005 K次取反后最大化的数组和

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort(key = lambda x: abs(x), reverse = True)

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
            
        for j in range(k):
            nums[-1] *= -1
        
        return sum(nums)