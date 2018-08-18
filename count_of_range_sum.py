class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        summ = [nums[0]]
        for el in nums[1:len(nums)]:
            summ.append(summ[len(summ) - 1] + el)
        #print(summ)

        def crSum(lo, hi):
            if lo == hi:
                if summ[lo] >= lower and summ[lo] <= upper:
                    #print('0..{}'.format(lo))
                    return 1
                else:
                    return 0
            mid =(hi + lo)//2 # [lo..mid],[mid+1..hi]
            count = crSum(lo,mid) + crSum(mid+1, hi)
            i=mid+1
            j=mid+1
            for el in summ[lo: (mid+1)]:
                #count sequences cross mid
                while (i<=hi) and ((summ[i]-el)<lower):
                    i= i + 1
                while j<=hi and (summ[j]-el) <= upper:
                    j = j + 1
                count = count + (j-i)
            # ---------sort summ[lo,hi]
            summ_l = []
            summ_r = []
            for el in summ[lo : (mid+1)]:
                summ_l.append(el)
            for el in summ[mid+1: hi+1]:
                summ_r.append(el)
            i = 0
            j = 0
            k = lo
            while i<(mid - lo +1) and j < (hi - mid):
                if summ_l[i]<summ_r[j]:
                    summ[k] = summ_l[i]
                    i = i + 1
                else:
                    summ[k] = summ_r[j]
                    j = j + 1
                k = k + 1
            if i==(mid - lo +1):
                while j < (hi - mid):
                    summ[k] = summ_r[j]
                    j = j + 1
                    k = k + 1
            else:
                while i<(mid - lo +1):
                    summ[k] = summ_l[i]
                    i += 1
                    k += 1
            #print(summ)
            # ---------sort summ[lo,hi]
            return count

        return crSum(0,len(summ)-1)
        '''
        l = len(nums)
        count = 0
        summ = [[0 for i in range(l)] for j in range(l)]
        tags = [[False for i in range(l)] for j in range(l)]
        for i in range(l):
            summ[i][i] = nums[i]
            if  nums[i] >= lower and nums[i] <= upper:
                    tags[i][i] = True
                    count = count + 1

        for x in range(1,l):
            for i in range(0,l-x):
                j = i + x
                summ[i][j]=summ[i][j-1] + nums[j]
                if summ[i][j]>=lower and summ[i][j]<=upper:
                    tags[i][j] = True
                    count = count + 1
        return count
        '''

if __name__ == '__main__':
    a = Solution()
    print(a.countRangeSum([-1,3,-2,1,5,7,-11,2],2,3))