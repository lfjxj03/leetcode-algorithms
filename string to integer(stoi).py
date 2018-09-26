class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = (2**31)-1
        MIN_INT = -(2**31)
        def getNum(str):
            i = 0
            try:
                while (i < len(str)) and (str[i] in {'0','1','2','3','4','5','6','7','8','9'}):
                    i += 1
                return int(str[0:i])
            except ValueError:
                return 0

        myRresult = 0
        length = len(str)
        if length == 0:
            return myRresult
        for i in range(length):
            if str[i] != ' ':
                break
        if i == length:
            return myRresult
        elif str[i] == '-' and i < length:
            myRresult = -getNum(str[i+1:])
        elif str[i] == '+' and i < length:
            myRresult = getNum(str[i+1:])
        else:
            myRresult = getNum(str[i:])# maybe numbers without sign, or not numbers
        if myRresult> MAX_INT:
            return MAX_INT
        elif myRresult< MIN_INT:
            return MIN_INT
        else:
            return myRresult


if __name__ == '__main__':
    print(Solution().myAtoi('034'))
    print(Solution().myAtoi('-034'))
    print(Solution().myAtoi('4193 with words'))
    print(Solution().myAtoi('words and 987'))
    print(Solution().myAtoi('-91283472332'))


