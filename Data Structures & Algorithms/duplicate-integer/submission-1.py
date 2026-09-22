class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = set()
        for i in range(len(nums)): 
            if nums[i] in hash_nums:
                return True; 
            else:
                hash_nums.add(nums[i])
        
        return False; 