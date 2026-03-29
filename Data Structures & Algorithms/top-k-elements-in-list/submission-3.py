class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ls = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        for n, c in dic.items():
            ls[c].append(n)

        ans = []
        for i in range(len(nums), 0, -1):
            for n in ls[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans