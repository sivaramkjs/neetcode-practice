class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force: 
        #   1. Create a hash map with key as sorted string version and value as list of all strings equal to the sorted string.
        #   2. Iterate through the input array.
        #   2. Sort each string.
        #   3. Check if it's already in the hash map. If so, append it to the value list, else add it to the hash map. 
        #   4. Return the list of values in the hash map.
        #   T: O(m * nlogn); m - number of strings, n - length of longest string

        if len(strs) == 1:
            return [strs]

        grouped_anagrams = defaultdict(list)
        start_lower_case_index = ord('a')
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - start_lower_case_index] += 1
            
            grouped_anagrams[tuple(count)].append(s)

        return list(grouped_anagrams.values())
