class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [c.lower() for c in s if c.isalnum()]
        for i in range(len(l)//2):
            if l[i]!=l[-i-1]: return False
        return True