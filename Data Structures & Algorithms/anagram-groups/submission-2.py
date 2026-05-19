from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            dic["".join(sorted(string))].append(string)
        

        ans = []
        for key, val in dic.items():
            ans.append(val)

        return ans