class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        
        ones = {1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine "}
        less_twenty = {11: "Eleven ", 12: "Twelve ", 13: "Thirteen ", 14: "Fourteen ", 15: "Fifteen ", 16: "Sixteen ", 17: "Seventeen ", 18: "Eighteen ", 19: "Nineteen "}
        tens = {10: "Ten ", 20: "Twenty ", 30: "Thirty ", 40: "Forty ", 50: "Fifty ", 60: "Sixty ", 70: "Seventy ", 80: "Eighty ", 90: "Ninety "}
        counts = {1: "Thousand ", 2: "Million ", 3: "Billion "}
        
        output = ""
        count = 0
        stack = []
        while(num):
            cur = num % 1000
            num /= 1000
            
            hundred = cur / 100
            ten = (cur % 100) / 10
            one = cur % 10
            
            section = ""
            if hundred:
                section += ones[hundred] + "Hundred "
            if ten:
                if ten == 1 and one:
                    section += less_twenty[10 + one]
                else:
                    section += tens[10 * ten]
            if one and ten != 1:
                section += ones[one]
            if count and cur:
                section += counts[count]
                
            count += 1
            stack.append(section)
        
        while(stack):
            output += stack.pop()
        
        return output[:-1]
                
