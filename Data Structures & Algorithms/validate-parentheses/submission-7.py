class Solution:
    def isValid(self, s: str) -> bool:
        """
        s = "({[ ]})"

        s must be an even length to be valid

        """

        if len(s) % 2 != 0:
            return False

        stack = []

        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            else:
                if stack:
                    check = stack.pop()
                else:
                    return False

                if c == "]" and check == "[":
                    continue
                elif c == "}" and check == "{":
                    continue
                elif c == ")" and check == "(":
                    continue
                else:
                    return False
        if stack:
            return False
        return True





