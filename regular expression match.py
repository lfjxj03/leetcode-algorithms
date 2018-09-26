class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isMatch2(s,p):
            """
            recursive version, slow
            :param s:
            :param p:
            :return: bool
            """
            if not p:
                return not s
            i = 0
            j = 0
            while i < len(p):
                if len(s[j:]) == 0:
                    if len(p[i:])==1:
                        return False
                    elif p[i+1] == '*':
                        return isMatch2(s[j:],p[i+2:])
                    else:
                        return False
                cmatch = p[i] in {s[j],'.'}# current match
                if i+1<len(p) and p[i+1] == '*':
                    if cmatch:
                        return isMatch2(s[j:],p[i+2:]) or isMatch2(s[j+1:],p[i+2:]) or isMatch2(s[j+1:], p[i:])
                    else:
                        return isMatch2(s[j:],p[i+2:])
                if cmatch:
                    j += 1
                    i += 1
                else:
                    return False
            return not s[j:]

        def isMatch1(s,p):
            """
            DP version, fast
            :param s:
            :param p:
            :return: bool
            """
            def updateStar(j,i):
                """
                x  ...<-> y * ...
                /\       /\
                |        |
                j        i
                :param i: index for pattern
                :param j: index for string
                :return: bool
                """
                tag = p[i] in {s[j], '.'}  # x...<->y*...
                sp[j][i] = (sp[j][i + 2] or sp[j + 1][i] ) if tag else sp[j][i + 2]

            def updateChar(j,i):
                """
                x  ...<-> y  ...
                /\       /\
                |        |
                j        i
                :param i: index for pattern
                :param j: index for string
                :return: bool
                """
                sp[j][i] = p[i] in {s[j], '.'} and sp[j + 1][i + 1]

            if not p:
                return not s
            sp = [[False for i in range(len(p)+1)] for j in range(len(s) + 1)]# +1 for ' ' at the end of s and p
            i = len(p)#p[len(p)]=' '
            j = len(s)#s[len(s)] = ' '
            sp[j][i] = True# ' ' match ' '. And sp[0][i],...sp[j-1][i] are already set to False
            k = i-1
            while k>=0:
                # compute sp[len(s)][0..len(p)-1]
                if p[k] == '*':
                    sp[j][k-1]= sp[j][k+1]
                    k = k-2
                else:
                    sp[j][k] = False# mismatch, because p[k]=x or '.', while s[j]=' '
                    k -= 1
            if j == 0 :
                return sp[0][0]
            else:
                j -= 1
                i -= 1
            while True:
                # 0<=i<len(p) and 0<=j<len(s)
                # step1: compute sp[j][i](or if p[i]=='*', compute sp[j][i-1])
                if p[i] == '*':
                    i -= 1# i index to c before '*'
                    updateStar(j,i)
                else:
                    updateChar(j,i)
                # step2: compute sp[0..j-1][i]
                l = j - 1
                if (i + 1) < len(p) and p[i+1] == '*':
                    while l>=0:
                        updateStar(l,i)
                        l -= 1
                else:
                    while l>=0:
                        updateChar(l,i)
                        l -= 1

                # step3: compute sp[j][0..i-1]
                k = i - 1
                while k >=0:
                    if p[k] == '*':
                        updateStar(j,k-1)
                        k -= 2
                    else:
                        updateChar(j,k)
                        k -= 1
                #step4:  update i , j  to valid values. if complete compution, break
                if j == 0 or i == 0:
                    return sp[0][0]
                else:
                    i -= 1
                    j -= 1

        return isMatch1(s,p)

if __name__ == "__main__":
    print(Solution().isMatch('a','ab*'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('ab','.*'))
    print(Solution().isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c"))
    print(Solution().isMatch('mississippi', 'mis*is*p*.'))

