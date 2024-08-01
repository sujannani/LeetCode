class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for det in details:
            if int(det[11:13])>60:
                c+=1
        return c