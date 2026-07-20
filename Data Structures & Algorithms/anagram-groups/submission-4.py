class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = collections.defaultdict(list)

        for word in strs:
            chars = [0 for _ in range(26)]
            for char in word:
                chars[ord(char) - ord("a")] += 1
            d[tuple(chars)].append(word)
        
        for value in d.values():
            ans.append(value)
        
        return ans
