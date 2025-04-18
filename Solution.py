class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"  # Base case for n = 1

        for _ in range(n - 1):  # Loop n-1 times
            temp = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                temp += str(count) + result[i]
                i += 1
            result = temp

        return result
# By Coding Moves
