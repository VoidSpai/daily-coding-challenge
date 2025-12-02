from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Create an empty dictionary
        
        for index, value in enumerate(nums):
            needed = target - value  # Calculate the number we need
            
            if needed in seen:
                # Found the pair
                return [seen[needed], index]
            
            # Store the current number with its index
            seen[value] = index