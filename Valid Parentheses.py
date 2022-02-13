class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        checking = False

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" and len(stack) > 0:
                if stack.pop() == "(":
                    checking = True
                else:
                    checking = False
                    break
            elif i == "]" and len(stack) > 0:
                if stack.pop() == "[":
                    checking = True
                else:
                    checking = False
                    break
            elif i == "}" and len(stack) > 0:
                if stack.pop() == "{":
                    checking = True
                else:
                    checking = False
                    break
            else:
                checking = False
                break
        if len(stack) > 0:
            return False
        return checking
