class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        for n, c in dic.items():
            count[c].append(n)
        

        ans = []
        for i in range(len(nums), 0, -1):
            for n in count[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        