class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
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


if __name__ == '__main__':
    a = Solution()
    print(a.countRangeSum([-1,3,-2,5,7,2],2,3))