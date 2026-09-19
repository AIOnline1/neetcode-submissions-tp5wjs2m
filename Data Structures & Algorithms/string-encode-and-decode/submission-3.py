class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded
    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
        
            length = int(s[i:j])
        
            start = j + 1
            end = start + length
            ls.append(s[start:end])

            i = end
        
        return ls
