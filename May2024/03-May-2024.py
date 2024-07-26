class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        v1=[int(i) for i in v1]
        v2=[int(i) for i in v2]
        i=0
        while(i<len(v1) and i<len(v2)):
            if v1[i]<v2[i]:
                return -1
            elif v1[i]>v2[i]:
                return 1
            i+=1

        while i<len(v1):
            if v1[i]!=0:
                return 1
            i+=1
        while i<len(v2):
            if v2[i]!=0:
                return -1
            i+=1
        return 0