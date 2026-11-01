class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        l=0
        for r in range(len(s2)):
            
            c = s2[r]
            d[c]-=1
            # print(d)
            
            if d[c]>=0: #if c is part of target chars
                if r-l+1==len(s1):
                    return True
            else: 
                #move l, update dict wrt removed char
                while(d[c]<0):
                    d[s2[l]]+=1
                    l+=1
        return False