class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the list of dictionary words into a set for O(1) lookups
        word_set = set(wordDict)
        
        # Create a DP array "dp" where dp[i] means:
        # "Is it possible to form the substring s[:i] from words in the dictionary?"
        dp = [False] * (len(s) + 1)
        
        # Base case: an empty substring can always be formed (by taking no words)
        dp[0] = True
        
        # Build up the dp array
        for i in range(1, len(s) + 1):
            for j in range(i):
                # Check if s[j:i] (the substring from index j to i-1) is in the dictionary
                # and if the substring up to j can be formed
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further once we know dp[i] is True
        
        return dp[-1]

