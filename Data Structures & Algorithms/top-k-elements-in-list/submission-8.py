class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ls = [[] for i in range(len(nums))]

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        for key, val in dic.items():
            ls[val - 1].append(key)

        ans = []
        
        for i in range(len(nums) - 1, -1, -1):
            for val in ls[i]:
                if len(ans) == k:
                    return ans
                ans.append(val)
        
        return ans