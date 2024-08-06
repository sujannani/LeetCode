class Solution:
    def minimumPushes(self, word: str) -> int:
        d=Counter(word)
        dNum=dict()
        m=2
        for f in sorted(d.items(),key=lambda x:-x[1]):
            if m not in dNum:
                dNum[m]=[f[0]]
            else:
                dNum[m].append(f[0])
            m+=1
            if m==10:
                m=2
        res=0
        for f in dNum:
            for k in range(len(dNum[f])):
                res+=d[dNum[f][k]]*(k+1)
        return res