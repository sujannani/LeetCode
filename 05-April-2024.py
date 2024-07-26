class Solution:
    def makeGood(self, s: str) -> str:
        sta=[]
        for i in s:
            if(len(sta)!=0):
                if ord(i)-ord('a')+32==ord(sta[-1])-ord('a') or ord(i)-ord('a')==ord(sta[-1])-ord('a')+32:
                    sta.pop()
                else:
                    sta.append(i)
            else:
                sta.append(i)
            print(''.join(sta))
        return ''.join(sta)