class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 2:
            return [0, 1]

        complements = {}
        for i in range(n):
            if nums[i] in complements:
                return [complements[nums[i]], i]
            current_complement = target - nums[i]
            # In case of duplicate numbers, below condition wiill help retaining 
            # the smallest index of both all indices of the duplicate number in the traversal order
            if not current_complement in complements:
                complements[current_complement] = i
        return []

        