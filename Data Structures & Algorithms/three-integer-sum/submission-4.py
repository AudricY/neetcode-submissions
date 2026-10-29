class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        targets = {}
        l = len(nums)
        for i in range(l):
            targets[-nums[i]] = i
        # print(targets)
        for i in range(l):
            for j in range(i+1,l,1):
                k = targets.get(nums[i]+nums[j],-1)
                if k != -1 and k != i and k != j:
                    triplet = tuple(sorted((nums[i],nums[j], nums[k])))
                    ans.add(triplet)
        return [list(t) for t in ans]

        