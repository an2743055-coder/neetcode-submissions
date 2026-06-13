class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       from collections import defaultdict
       anagram_map=defaultdict(list)
       for words in strs:
        sorted_keys="".join(sorted(words))
        anagram_map[sorted_keys].append(words) 
       return list(anagram_map.values())
            
            
            