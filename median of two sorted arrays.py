class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1)>len(nums2):
            #make sure that array1 is shorter than array2
            array1=nums2
            array2=nums1
        else:
            array1 = nums1
            array2 = nums2
        len1 = len(array1)
        len2 = len(array2)
        try:
            init_min = min(array1[0],array2[0])
            init_max = max(array1[len1 -1], array2[len2 -1])
        except IndexError:
            if len2==0:
                raise IndexError
            else:
                return (array2[(len2-1)//2] + array2[len2//2])/2

        left1 = 0 # position index
        right1 = 2 * len1 # position index
        while left1 <= right1:
            mid1 = (right1 + left1)//2
            mid2 = len1 + len2 - mid1
            l1 = init_min if mid1==0 else array1[(mid1 - 1)//2]#(mid1 - 1)//2 is num index
            r1 = init_max if mid1==2*len1 else array1[mid1//2]#(mid1 - 1)//2 is num index
            l2 = init_min if mid2 == 0 else  array2[(mid2 - 1) // 2]# (mid1 - 1)//2 is num index
            r2 = init_max if mid2 == 2*len2 else array2[mid2 // 2]  # (mid1 - 1)//2 is num index

            if l1>r2:
                right1= mid1 - 1
            elif l2 > r1:
                left1 = mid1 + 1
            else:
                return (max(l1,l2) + min(r1,r2))/2

if __name__ == '__main__':
    s =Solution()
    print(s.findMedianSortedArrays([2,4,7],[0,2,3]))




