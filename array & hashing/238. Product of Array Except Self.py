#238. Product of Array Except Self  
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#time complexity: O(n)
#space complexity: O(1)
#https://leetcode.com/problems/product-of-array-except-self/

nums = [1,2,3,4]

output = []
prefix = 1
for n in nums:
    output.append(prefix) #append the prefix to the output list  
    prefix *= n #update the prefix by multiplying it by the current element in the list 
print(output)   #output is [1, 1, 2, 6]
postfix = 1 #initialize postfix to 1
for i in reversed(range(len(nums))):   #iterate through the list in reverse order main idea is to multiply the output list with the postfix list 
    output[i] *= postfix #multiply the output list with the postfix list    
    postfix *= nums[i] #update the postfix by multiplying it by the current element in the list
print(output)   #output is [24, 12, 8, 6]