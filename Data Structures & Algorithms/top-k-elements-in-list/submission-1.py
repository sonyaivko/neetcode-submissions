class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_nums_map:
                hash_nums_map[nums[i]] = 0
            
            hash_nums_map[nums[i]] += 1
        
        #to sort by value, key=lambda x: hash_nums_map[x]
        # to sort in descending order: reverse=True 
        hash_nums_map = sorted(hash_nums_map, key=lambda x: hash_nums_map[x], reverse=True)
        print(hash_nums_map)
        return hash_nums_map[0:k]


