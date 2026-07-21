class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for key, val in dic.items():
            freq[val].append(key)

        ans = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans            
            
