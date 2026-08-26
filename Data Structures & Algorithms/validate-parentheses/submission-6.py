class Solution:
    def isValid(self, s: str) -> bool:
        check =  { ")" : "(", "]" : "[", "}" : "{" }
        stack= []
        for each in s:
            if each in check:
                if not stack or stack[-1] != check[each]:
                    return False
                stack.pop()
            else:
                stack.append(each)
        return True if not stack else False