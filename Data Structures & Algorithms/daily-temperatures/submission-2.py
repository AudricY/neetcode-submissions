class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0]*l
        s = []
        for i in range(l):
            # print(s)
            t = temperatures.pop(0)
            if s:
                # print(s[-1][1])
                while s and t>s[-1][1]:
                    (i2,t2) = s.pop(-1)
                    res[i2] = i-i2
            s.append((i,t))
        return res


        