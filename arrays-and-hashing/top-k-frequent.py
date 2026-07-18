import heapq


# Heap solution
# N = length of nums
# M = number of unique elements (M <= N)
# Time:   O(N + M log K)
# Space:  O(N)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n in count.keys():
            heapq.heappush(heap, (count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [n for c, n in heap]


# Bucket sort solution
# Time:   O(N)
# Space:  O(N)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
