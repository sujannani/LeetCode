class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        st=''
        res=0
        for s in arr:
            if arr.count(s)==1:
                res+=1
                st=s
            if res==k:
                return st
        return ''