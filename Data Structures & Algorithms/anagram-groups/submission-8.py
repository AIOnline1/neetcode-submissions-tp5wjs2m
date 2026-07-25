class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}


        for string in strs:
            alphabet = [0 for _ in range(26)]
            for char in string:
                alphabet[ord(char) - ord('a')] += 1
            
            if tuple(alphabet) in dic:
                dic[tuple(alphabet)].append(string)
            else:
                dic[tuple(alphabet)] = [string]
            
        ans = []

        for value in dic.values():
            ans.append(value)
        
        return ans