class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# tried sorting approach. So basicaly sort the array and then check if the adjacent elements are same or not. If they are same then return True else return False. This approach is O(nlogn) because of sorting.
