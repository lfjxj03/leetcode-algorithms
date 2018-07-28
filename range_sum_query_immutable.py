class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.len = len(nums)
        self.dp = self.getDp()
    def getDp(self):
        if self.len == 0:
            return []
        else:
            dp = [0 for i in range(self.len)]
            dp[0] = self.nums[0]
            for i in range(1,self.len):
                dp[i] = dp[i-1] + self.nums[i]
            return dp

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        assert i<=j, 'Error:i>j!'
        assert i>=0, 'Error: i<0!'
        assert j<self.len, 'Error: j> length of nums!'
        result=0
        result = self.dp[j]-self.dp[i] + self.nums[i]
        return result
if __name__ == '__main__':
    a = NumArray([3,4,2,-2])
    print(a.sumRange(2,2))
    print(a.sumRange(0,3))
    print(a.sumRange(0,2))