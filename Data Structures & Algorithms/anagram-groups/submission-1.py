class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count_key = tuple(count)
            if count_key not in hashmap:
                hashmap[count_key] = []
            hashmap[count_key].append(s)
        return list(hashmap.values())


            