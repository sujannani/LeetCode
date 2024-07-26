class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score)==0:
            return []
        temp=score.copy()
        temp.sort()
        d=dict()
        d[temp[-1]]="Gold Medal"
        if len(score)==1:
            return [d[temp[-1]]]
        d[temp[-2]]="Silver Medal"
        if len(score)==2:
            return [d[score[0]],d[score[1]]]
        d[temp[-3]]="Bronze Medal"
        for i in range(len(score)-4,-1,-1):
            d[temp[i]]=str(len(score)-i)
        
        res=[]
        for i in score:
            res.append(d[i])
        return res

#506