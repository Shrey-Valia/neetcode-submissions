class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while len(nums) > 0:
            num = nums.pop(0)
            print(nums)
            if num in nums:
                return True
        return False