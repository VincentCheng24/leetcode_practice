import numpy as np
import time

class Solution:
    def removeElement_v1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # n = len(nums)
        # nums.sort()
        st = time.time()
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                i -= 1
            i += 1

        return len(nums), time.time()-st

    def removeElement_v2(self, nums, val):
        st = time.time()

        idx = [i for i in range(len(nums)) if nums[i] == val]

        for i in idx:
            nums.remove(nums[i])

        return len(nums), time.time()-st


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums2 = [i for i in range(10000)]
solver = Solution()
print('%.20f' % (solver.removeElement_v1(nums2, 3))[1])
print('%.20f' % (solver.removeElement_v2(nums2, 3))[1])

