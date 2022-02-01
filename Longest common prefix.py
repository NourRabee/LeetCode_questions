class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        if len(strs) == 1:
            return prefix

        else:
            commonprefix = ""
            for i in zip(*strs):
                if (len(set(i)) != 1):
                   break
                else:
                    commonprefix += i[0]
                    
            return commonprefix
