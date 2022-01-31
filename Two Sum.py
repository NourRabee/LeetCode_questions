class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_hashMap = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen_hashMap:
                return [i, seen_hashMap[remaining]]

            seen_hashMap[value] = i
 

#solving using hashmap
