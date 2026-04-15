class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        result = []
        frequency_map = defaultdict(int)    
        for num in nums:
            frequency_map[num] += 1
        
        # bucket sort using bucket index as frequency and each bucket containing all numbers with that index frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in frequency_map.items():
            buckets[val].append(key)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
