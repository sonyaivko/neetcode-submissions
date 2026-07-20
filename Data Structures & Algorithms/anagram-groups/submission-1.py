class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # empty hashmap
        sorted_anagrams = {}

        # sorted_s is the value 
        for s in strs:
            sorted_s = "".join(sorted(s))

            # if string is not already there, new list 
            if sorted_s not in sorted_anagrams:
                sorted_anagrams[sorted_s] = []
            
            # add the true string to the list by its KEY value 
            sorted_anagrams[sorted_s].append(s)
        
        return list(sorted_anagrams.values())
