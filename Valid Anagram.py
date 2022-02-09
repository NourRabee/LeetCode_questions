class Solution:
    
    def counts(string):
        
        c_dict = {}
        
        for i in string:
            if i in c_dict:
                c_dict[i] = c_dict[i] + 1
            else:
                c_dict[i] = 1
        return c_dict

    def isAnagram(self, s: str, t: str) -> bool:
        
        if Solution.counts(s) == Solution.counts(t):
            return True
        else:
            return False
          
        
#         temp = ""
#         if len(t) != len(s):
#             return False
        
#         for i in s:
#             if s.count(i) == t.count(i):
#                 temp +=i
#                 s.replace(i, "")
#                 t.replace(i, "")
#         if temp == s:
#             return True
#         else:
#             return False

