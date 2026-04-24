class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # loop through and for each window keep track of the mostf char 
        # window is valid if len(window) - mostf <= k 
        # if a window is valid we can expand 
        # if a window is invalid shrink it 

        longest = 0

        # keep track of most freq in a window 
        mostf = 0

        # keep a map of char counts
        count = defaultdict(int)

        # left and right pointers to move our window
        l = r = 0

        # until the right pointer reaches the end 
        while r < len(s):
            count[s[r]] += 1
            if count[s[r]] > mostf:
                mostf = count[s[r]]

            if r - l + 1 - mostf <= k:
                longest = max(longest, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
            r += 1
        return longest
            