class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for c in s:
            if c in "[{(":
                stack.append(c)
            else:
                if not stack: return False
                out = stack.pop(-1)
                print(out)
                if out!=m[c]: return False
        if len(stack)!=0: return False
        return True