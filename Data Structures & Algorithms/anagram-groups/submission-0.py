class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key =  "".join(sorted(word)) # sorted letters as a string
           
 
            if key not in groups:
                groups[key] =  [] # Start an empty list
            groups[key].append(word) # add this word to its group

        return list(groups.values())
            