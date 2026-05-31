from _heapq import heappush
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []

        # hashmap storing indexes
        idx_hashmap = {}

        for idx, num in enumerate(nums):
            idx_hashmap[num] = idx

        # use a complement to determine the pair
        for i in range(0, len(nums)):

            complement = target - nums[i]

            if complement in idx_hashmap and i != idx_hashmap[complement]:

                return [i, idx_hashmap[complement]]