class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        res=""
        for i in range(len(word)):
            if word[i]==ch:
                res=word[i]+res
                break
            else:
                res=word[i]+res
        res+=word[i+1:]
        return res

#2000 ques
            