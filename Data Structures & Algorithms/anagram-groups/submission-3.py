class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map_strs = {}

        for s in range(len(strs)):
            sorted_s = "".join(sorted(strs[s]))
            if sorted_s not in hash_map_strs:
                hash_map_strs[sorted_s] = []
            
            hash_map_strs[sorted_s].append(strs[s])
        
        return sorted(hash_map_strs.values())
                