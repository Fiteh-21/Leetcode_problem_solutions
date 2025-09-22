class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for x in range(n):
            new_nums = []
            for i in range(n):
                new_nums.append(nums[(i+x) % n ])
            if new_nums == sorted(nums):
                return True
        return False