class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        # sort each word 
        for word in strs:
            key = tuple(sorted(word))
         # build a key from letter counts instead of sorting
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)

            # if key is new, start it with an empty list
            if key not in hashmap:
                hashmap[key] = []
            # append the original word 
            hashmap[key].append(word)

        # return the hashmap values 
        return list(hashmap.values())