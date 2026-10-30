class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pbuy=prices[0]
        psell=0
        ans=0
        for i in range(1, len(prices)):
            pcur = prices[i]
            if pcur<pbuy:
                pbuy=pcur
                psell=0
            else:
                psell=pcur
            profit=psell-pbuy
            ans=max(profit,ans)
        return ans


        