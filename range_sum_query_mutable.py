class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #build Fenwick tree, elem with index=0 is discarded
        self.nums = [0]
        for el in nums:
            self.nums.append(el)
        self.lens = len(self.nums)
        self.tree=[0 for i in range(self.lens)]
        for i in range(1,(self.lens)):
            self._addt(i,self.nums[i])


    def _addt(self,i,x):
        '''
        add x to self.tree[i] and its right higher nodes
        :param i: index
        :param x:
        :return: void
        '''
        index = i
        while index< self.lens:
            self.tree[index] += x
            index += index&(-index)
    def _sumn(self,i):
        '''
        sum from self.nums[1] to self.nums[i]
        :param i:
        :return: sum
        '''
        index = i
        sum = 0
        while index>0:
            sum = sum + self.tree[index]
            index -= index & (-index)
        return sum

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        old = self.nums[i+1]
        self.nums[i+1] = val
        self._addt(i+1,val-old)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return (self._sumn(j+1) - self._sumn(i))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
if __name__ == '__main__':
    obj = NumArray([1,2,3,4,5,6,7,8])
    print(obj.sumRange(0,5))
    obj.update(0,3)
    print(obj.sumRange(0,5))
