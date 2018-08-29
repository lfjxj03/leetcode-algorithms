class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        b = 0# begin for each substring without repeat characters
        i = 0# search pointer
        slen=0# longest length of substring until now
        string = ''
        while i <length:
            if string.find(s[i])== -1:
                string = string + s[i]
                i += 1
            else:
                if slen < (i-b):
                    slen = i - b
                po = string.find(s[i])
                b = b + po + 1# new substring may begin from the next char of first appear of the repeat char
                string = string[(po+1):]
                string = string + s[i]
                i += 1
        if slen < (i - b):
            slen = i - b
        return slen

if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLongestSubstring('sbdefsfxyzwef'))


