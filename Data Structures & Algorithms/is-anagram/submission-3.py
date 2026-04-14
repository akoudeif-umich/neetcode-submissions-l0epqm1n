class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = defaultdict(int)
        word2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            word1[s[i]] += 1
            word2[t[i]] += 1
        
        return word1 == word2