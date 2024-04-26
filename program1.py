class Solution(object):
  
    def isValid(self, s):
        stack = [] 
        for c in s: # loop through each character in the string
            if c in '([{': 
                stack.append(c) # push it onto the stack
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False 
                stack.pop()
        return not stack 
    



  

