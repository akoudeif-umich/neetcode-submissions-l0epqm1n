class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Brute force:
        a nested loop where the inner loop finds a hotter day 
        appends it and breaks

        # does going backwards help me at all?
        # last number always has to be a 0 

        """

        stack = []

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr = temperatures[i]

            while stack and curr > temperatures[stack[-1]]:
                cold = stack.pop()
                res[cold] = i - cold
            stack.append(i)
        return res