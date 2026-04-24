class Solution:
    def isPalindrome(self, l, r, s, res):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1
    
        return res
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            res = self.isPalindrome(i, i, s, res)
            res = self.isPalindrome(i, i + 1, s, res)

        return res