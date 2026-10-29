class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        sorted_data = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        # print(sorted_data)
        res = []
        for i in range(k):
            res.append(sorted_data[i][0])
        return res
