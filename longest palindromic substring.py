class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l<=1:
            return s
        i = 0
        max_sidelen = 0# substring = leftside + s[i] + rightside
        max_symlen = 0# substring = leftside + rightside
        low_si, high_si, low_sy, high_sy= 0, 0, 0, 0# low index and high index
        while (i + max_sidelen) < (l-1):
            # find *#* pattern
            i += 1
            j = 1
            while (i-j)>=0 and (i+j)<=(l-1):
                if s[i-j] == s[i+j]:
                    j += 1
                else:
                    break
            if (j-1) > max_sidelen:
                max_sidelen = j-1
                low_si = i-(j-1)
                high_si = i + (j-1)
        i = 0
        while (i + max_symlen -1) < (l-1):
            # find **|** pattern
            i += 1
            j = 1
            while (i-j)>=0 and (i+j-1)<=(l-1):
                if s[i-j] == s[i+j-1]:
                    j += 1
                else:
                    break
            if (j-1)>max_symlen:
                max_symlen = j-1
                low_sy = i-(j-1)
                high_sy = i + (j-1) -1

        if (max_symlen*2) < (max_sidelen*2 +1):
            return s[low_si:(high_si + 1)]
        else:
            return s[low_sy:(high_sy + 1)]

if __name__ == "__main__":
    print(Solution().longestPalindrome('aabbccbccba'))
    print(Solution().longestPalindrome(''))
    print(Solution().longestPalindrome('aa'))
    print(Solution().longestPalindrome('bbbaabbb'))