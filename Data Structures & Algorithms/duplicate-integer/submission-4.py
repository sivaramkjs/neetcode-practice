class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        
        return False