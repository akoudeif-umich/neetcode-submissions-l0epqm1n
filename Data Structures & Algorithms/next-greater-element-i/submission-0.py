class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        greater = {}

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and curr > stack[-1]:
                temp = stack.pop()
                greater[temp] = curr

            stack.append(curr)

        for num in nums1:
            if num in greater:
                res.append(greater[num])
            else:
                res.append(-1)

        return res
        

