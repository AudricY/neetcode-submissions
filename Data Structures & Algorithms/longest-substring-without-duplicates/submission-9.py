class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ss = []
        ans=0
        for c in s:
            # print(d)
            # print(ss)
            present = d.get(c,0)
            ss.append(c)
            if present:
                while ss: 
                    popped = ss.pop(0)
                    d[popped] = 0
                    if popped==c: break
            else:
                ans = max(ans, len(ss))
                # print(ans)
            d[c] = 1
            # ss.append(c)
        return ans
        