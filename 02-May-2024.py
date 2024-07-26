class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res=-2**31
        for i in nums:
            if i>0 and -i in nums:
                res=max(res,i)
        return -1 if res<0 else res