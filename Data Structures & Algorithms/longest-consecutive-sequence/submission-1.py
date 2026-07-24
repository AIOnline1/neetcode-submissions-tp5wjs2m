class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set()
        ans = 0
        for num in nums:
            seen.add(num)


        for num in nums:
            counter = 0
            while num + 1 in seen:
                counter += 1
                num += 1
            
            ans = max(ans, counter)

        return ans + 1

            