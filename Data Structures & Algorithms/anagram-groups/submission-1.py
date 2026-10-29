class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        # sort each word 
        for word in strs:
            key = "".join(sorted(word))

            # if key is new, start it with an empty list
            if key not in hashmap:
                hashmap[key] = []
                        # append the original word 
            hashmap[key].append(word)

        # return the hashmap values 
        return list(hashmap.values())