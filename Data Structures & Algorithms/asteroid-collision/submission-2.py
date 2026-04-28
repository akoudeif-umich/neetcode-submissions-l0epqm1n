class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []


        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < a * -1:
                    stack.pop()
                elif stack[-1] > a * -1:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack