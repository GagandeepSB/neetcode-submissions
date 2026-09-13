class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for n in range(len(nums)):
            difference = target - nums[n]
            if difference in seen:
                return [seen[difference], n]
            seen[nums[n]] = n
        return False