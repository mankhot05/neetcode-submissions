class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ours = {}
        ourt = {}
        for ch in s:
            ours[ch] = ours.get(ch, 0) + 1
        for ch in t:
            ourt[ch] = ourt.get(ch, 0) + 1
        if ourt == ours:
            return True
        return False