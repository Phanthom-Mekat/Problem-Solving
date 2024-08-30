class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums:
                try:
                    j = nums.index(another)
                    if i != j:
                        return [i, j]
                except ValueError as e:
                    continue
        return []


# another good approach

class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store the index of numbers
        num_to_index = {}
        
        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that would add up to the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If it is, we have found the two numbers
                return [num_to_index[complement], i]
            
            # Store the current number with its index in the dictionary
            num_to_index[num] = i
        
        # Return an empty list if no solution is found
        return []

# Example usage:
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
