import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l <= r:
            i = (r-l)//2+l
            print(l,r,i)
            if target>nums[i]:
                l = i+1
            elif target<nums[i]:
                r = i-1
            else:
                return i
        return -1

        