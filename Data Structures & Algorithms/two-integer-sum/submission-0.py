class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dic = {}

       # when we subtract curr number from target
       # that is next index we need to find
    

       for i in range(len(nums)):
            val = target - nums[i]
 
            if nums[i] in dic:
                return sorted(list([i,dic[nums[i]]]))


            dic[val] = i

    



        