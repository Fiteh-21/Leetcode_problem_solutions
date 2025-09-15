class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        last_non_zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        for i in range(last_non_zero, n):
            nums[i] = 0