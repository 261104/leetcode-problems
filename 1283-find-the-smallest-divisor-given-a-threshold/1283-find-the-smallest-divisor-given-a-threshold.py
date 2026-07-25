import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Corrected list comprehension for summation
            total_sum = sum(math.ceil(n / mid) for n in nums)
            
            if total_sum > threshold:
                low = mid + 1
            else:
                ans = mid       # Record valid divisor
                high = mid - 1  # Try to find a smaller one
                
        return ans


            




        