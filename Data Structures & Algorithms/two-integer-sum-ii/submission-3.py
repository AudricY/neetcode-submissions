class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        sum = numbers[l] + numbers[r]
        while sum != target:
            if sum < target: l+=1
            else: r-=1
            sum = numbers[l] + numbers[r]
        return [l+1,r+1]
            


#12
#1 2 3 4 5 6 7 12