class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        integer= int(s)+1
        newList = []
        for i in str(integer):
            newList.append(i)
        return newList
