class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for string in strs:
            sortedString = str(sorted(string))

            if sortedString in dic:
                dic[sortedString].append(string)
            else:
                dic[sortedString] = [string]
        
        ans = []
        
        for val in dic.values():
            ans.append(val)

        return ans