class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            alphabet = [0 for _ in range(26)]
            for char in string:
                alphabet[ord('a') - ord(char)] += 1
            dic[tuple(alphabet)].append(string)
        
        ans = []
        for value in dic.values():
            ans.append(value)
        
        return ans