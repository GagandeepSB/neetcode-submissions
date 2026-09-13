class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #stores every element seen prior to current element
        # mapping == val: index --> mapping == seen(nums[i], i)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i 