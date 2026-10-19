from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        res = []
        cnt = 0
        for inner_bucket in buckets[::-1]:
            for e in inner_bucket:
                res.append(e)
                cnt += 1
                if cnt == k: return res
        return res

        