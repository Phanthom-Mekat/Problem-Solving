class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)
        raw_list = [0 for _ in range(min_num, max_num+1)]
        for num in nums:
            raw_list[num-min_num] += 1
        final_list = []
        for idx, v in enumerate(raw_list):
            if v > 0:
                final_list.extend([idx+min_num] * v)
        return final_list