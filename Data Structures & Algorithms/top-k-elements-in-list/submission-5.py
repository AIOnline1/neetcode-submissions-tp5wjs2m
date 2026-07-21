class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1


        ls = []
        for item in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:k]:
            ls.append(item[0])
        
        return ls
