class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nums = [x for row in matrix for x in row]
        l=0
        r=len(nums)-1
        while l <= r:
            i = (r-l)//2+l
            if target>nums[i]:
                l = i+1
            elif target<nums[i]:
                r = i-1
            else:
                return True
        return False