def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    
    # Create a 2D array to store the counts
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: There's one way to match an empty t with any prefix of s
    for i in range(m + 1):
        dp[i][0] = 1
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # Match or ignore
            else:
                dp[i][j] = dp[i - 1][j]  # Ignore s[i-1]

    return dp[m][n]

# Example usage
print(numDistinct("rabbbit", "rabbit"))  # Output: 3
print(numDistinct("palainpalani", "palani"))     # Output: 5
