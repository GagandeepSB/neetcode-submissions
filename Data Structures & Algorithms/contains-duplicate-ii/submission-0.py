class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time - O(n)
        # Space - O(n)
        Hmap = {} # Declare hashmap

        # Loop through the indices of the array
        for i in range(len(nums)):
            # Check if value in Hmap and if so check that abs value of current index
            # minus the index of the key (the matching element) is mapped to is <= k 
            if nums[i] in Hmap and abs(i - Hmap[nums[i]]) <= k:
                return True
            # Otherwise, element was not seen in the list, so add it
            # Add it in the form of the value maps to the index
            # This leads to easy indexation later
            else:
                Hmap[nums[i]] = i
        return False
        
            