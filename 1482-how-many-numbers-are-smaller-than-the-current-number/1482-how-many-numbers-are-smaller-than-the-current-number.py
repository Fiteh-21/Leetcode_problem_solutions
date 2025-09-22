class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smaller_num_list = []
        for i in range(n):
            count = 0
            for j in range(n):
                if (j != i) and (nums[i] > nums[j]):
                    count += 1
            smaller_num_list.append(count)
        return smaller_num_list