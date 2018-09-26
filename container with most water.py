class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        indexl = 0
        indexr = len(height) -1
        while indexl <= indexr:
            l = height[indexl]
            r = height[indexr]
            h = l if l <= r else r
            water1 = h * (indexr - indexl)
            if water1 > water:
                water = water1
            while indexl <= indexr and height[indexl] <= h: indexl += 1
            while indexr >= indexl and height[indexr] <= h: indexr -= 1
        return water

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))