# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Date: 2021-07-23 02:00:00
# Runtime: 92 ms, faster than 90.68% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.9 MB, less than 5.07% of Python3 online submissions for Top K Frequent Elements.
# (Note: Solution is in python3)
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Time complexity: O(nlogk)
# Space complexity: O(n)

from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                counter = Counter(nums) #the output will be a dictionary with the number of times each element appears in the list  
                return [i for i, _ in counter.most_common(k)] #return the k most common elements in the list as a list the elements are sorted in descending order of their frequency of occurence in the list the simplest way of the loop is for num, _ in counter.most_common(k): return num 