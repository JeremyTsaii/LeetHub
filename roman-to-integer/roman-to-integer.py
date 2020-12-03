class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        sum1 = 0
        while len(s)!=0:
            if s[:2] in memo:
                sum1 += memo[s[:2]]
                s = s[2:]
            elif s[0] in memo:
                sum1 += memo[s[0]]
                s = s[1:]
        return sum1
