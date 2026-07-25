class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in dic:
                dic[sortedString].append(string)
                continue
                
            dic[sortedString] = [string]
        
        ls = []
        for val in dic.values():
            ls.append(val)
        
        return ls