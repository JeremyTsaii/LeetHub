class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []
        for p in s:
            if p in dic:
                if not stack or stack[-1] != dic[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return len(stack) == 0
