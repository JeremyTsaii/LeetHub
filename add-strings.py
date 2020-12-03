class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = list(num1)
        l2 = list(num2)
        carry = 0
        output = ''
        while (l1 or l2 or carry):
            if l1:
                carry += ord(l1.pop())-ord('0')
            if l2:
                carry += ord(l2.pop())-ord('0')
            output =  str(carry%10) + output
            carry = carry//10
        return output
