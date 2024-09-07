#128 Longest Consecutive Sequence
#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#Your algorithm should run in O(n) complexity.

#Example:


#Input: [100, 4, 200, 1, 3, 2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


#Solution:
#1. Create a set of the input list
#2. Iterate through the set
#3. For each element, check if the element - 1 is in the set
#4. If it is, remove the element - 1 from the set
#5. Check if the element + 1 is in the set
#6. If it is, remove the element + 1 from the set
#7. Update the maximum length of the sequence
#8. Return the maximum length of the sequence

#Code:
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            s = set(nums)   
            q = 0   
            while s:
                n = s.pop() #By popping the number, we ensure that we don’t check the same number twice.
                l = n - 1
                while l in s:   
                    s.remove(l)
                    l-=1
                h = n + 1
                while h in s:
                    s.remove(h)
                    h+=1
                q = max(q, h-l-1)
            return q
