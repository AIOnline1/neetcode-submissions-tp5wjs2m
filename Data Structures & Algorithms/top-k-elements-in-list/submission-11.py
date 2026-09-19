class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        numbers = [[] for _ in range(len(nums))]

        for key, val in dic.items():
            numbers[val - 1].append(key)
        

        ls = []

        for i in range(len(nums) - 1, -1, -1):
            for val in numbers[i]:
                if len(ls) == k:
                    return ls
                ls.append(val)
        
        return ls