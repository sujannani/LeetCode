class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r=nums[0]
        for i in range(1,len(nums)):
            r=r^nums[i]
        
        r=r^k
        r=str(bin(r)[2:])
        return r.count('1')