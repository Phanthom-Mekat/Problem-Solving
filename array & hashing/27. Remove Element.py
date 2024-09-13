#27 remove element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.




class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)

        k = len(nums)
        return k

# Time complexity: O(n)
# Space complexity: O(1)

# test
nums = [3,2,2,3]
val = 3
s = Solution()
print(s.removeElement(nums, val)) # 2