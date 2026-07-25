class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ls = [[] for _ in range(len(nums))]

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for key, val in dic.items():
            ls[val - 1].append(key)


        ans = []
        print(ls)
        for i in range(len(ls) - 1, -1, -1):
            for num in ls[i]:
                while len(ans) < k:
                    ans.append(num)
                    break

        return ans

            
