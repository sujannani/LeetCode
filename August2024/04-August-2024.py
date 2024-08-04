class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subSums=[]
        for i in range(n):
            for j in range(i,n):
                subSums.append(sum(nums[i:j+1]))
        subSums.sort()
        res=0
        for i in range(left-1,right):
            res+=subSums[i]
            res=res%1000000007
        return res