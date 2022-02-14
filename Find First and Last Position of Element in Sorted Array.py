class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = {}
        indices = []
        result = []

        if target in nums:

            for i in range(len(nums)):
                position[i] = nums[i]

            for i in position:
                if position[i] == target:
                    indices.append(i)

            result.append(min(indices))
            result.append(max(indices))

            return result

        else:
            return [-1, -1]
