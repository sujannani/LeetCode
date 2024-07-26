class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        j=len(happiness)-1
        s=0
        res=0
        while j>=0 and (happiness[j]-s)>0 and k>0:
            res+=happiness[j]-s
            s+=1
            j-=1
            k-=1
        return res