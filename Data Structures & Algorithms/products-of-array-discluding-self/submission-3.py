class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        n_0 = nums.count(0)
        if n_0 >1: return res

        t_p = 1
        for n in nums:
            if n!=0:
                t_p*=n
        # print(t_p)

        if n_0 == 1:
            res[nums.index(0)] = t_p
        else:
            res = [int(t_p/i) for i in nums]
        return res


        

        