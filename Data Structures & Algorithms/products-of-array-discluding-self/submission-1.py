class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0 for _ in range(len(nums))]
        posf = [0 for _ in range(len(nums))]

        pref[0] = 1
        posf[-1] = 1
        for i in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]

        
        for i in range(len(nums) - 2, -1, -1):
            posf[i] = nums[i + 1] * posf[i + 1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(pref[i] * posf[i])

        return ans