class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sta=[]
        res=[]
        s=[x for x in s]
        for i in s:
            if i==")" and len(sta)==0:
                continue
            elif i=="(":
                sta.append(i)
                res.append(i)
            elif i==")":
                sta.pop()
                res.append(i)
            else:
                res+=i
        c=0
        for i in range(len(res)-1,-1,-1):
            if res[i]=="(" and c<len(sta):
                res[i]=""
                c+=1
        return ''.join(res)