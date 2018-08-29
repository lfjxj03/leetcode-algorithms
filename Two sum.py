class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    def test(self,x):
        if isinstance(x,str):
            y=len(x)
        elif isinstance(x,int):
            y = x
        print(y)

if __name__ == '__main__':
    Solution().test(5)