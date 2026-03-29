from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            s = tuple(sorted(string))

            dic[s].append(string)
        

        return [i for i in dic.values()]
        