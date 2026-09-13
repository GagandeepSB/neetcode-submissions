class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding Window Approach
        # By "abs(i - j) <= k" they mean the size of the window between the 2 elements is <= k
        
        # Initalize window hashset, which keeps track of all the values in the window
        window = set()
        # Left pointer of the window, right pointer initialized in for loop below
        l = 0

        # Loop through every element in the array
        for r in range(len(nums)):
            # Check if window is bigger than k, if so remove the left element in the window
            # Then increment left pointer to the right by 1
            if r - l > k:
                window.remove(nums[l])
                l += 1
            # If nums at r is in window, that means this element is a duplicate, so return true
            if nums[r] in window:
                return True
            # If the value is not in the window, then add it to our window
            window.add(nums[r])
        return False