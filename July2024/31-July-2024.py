class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        b=0
        for i in range(1,len(s)+1):
            if s[i-1]=='b':
                dp[i]=dp[i-1]
                b+=1
            else:
                dp[i]=min(b,dp[i-1]+1)
        return dp[-1]