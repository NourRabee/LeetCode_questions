class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        list = s.split()
        sum = 0

        for i in range(len(list)):
            if i == len(list)-1:
               for y in list[i]:
                   sum +=1
        return sum
