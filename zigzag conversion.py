class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        assert numRows>=0 ,'numRows < 0!'
        if numRows == 0 :
            return ''
        elif numRows == 1:
            return s
        else:
            out = ''
            for rows in range(numRows):
                i = rows#index of the first letter in row with the num rows
                while i<len(s):
                    out += s[i]
                    if (i-rows)%(2*numRows - 2)==0:
                        dis = (2*numRows - 2) - 2*rows# distance from current to the next one in same row
                        if dis == 0:# last row
                            dis = (2*numRows - 2)
                    else:
                        dis = 2*rows
                    i += dis
            return out
if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING',3))
    print(Solution().convert('PAYPALISHIRING',4))
    print(Solution().convert('PAYPALISHIRING', 1))
    print(Solution().convert('PAYPALISHIRING', 2))
