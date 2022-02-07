class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            index = 0

            if target in nums:
                index = nums.index(target)
            else:
                bisect.insort(nums, target)
                index = nums.index(target)
            return index
