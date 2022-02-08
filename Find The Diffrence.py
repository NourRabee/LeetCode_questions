class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        str1 = []
        str2 = []

        sub = ""
        for i in s:
            str1.append(i)
        for i in t:
            str2.append(i)

        temp = list(zip(str1, str2))
        for i in temp:
            str1.remove(i[0])
            str2.remove(i[0])
        if not str1:
            sub = str2[0]

        elif not str2:
            sub = str1[0]

        return sub

    
#    for i in t:
#        if s.count(i) != t.count(i):
#              return i
