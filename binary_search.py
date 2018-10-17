class Solution:
    def peakIndexInMountainArray_852(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        h = len(A) - 1
        l = 0

        while l <= h:
            m = (h + l) // 2
            if A[m+1] < A[m] > A[m-1]:
                return m
            elif A[m+1] > A[m] > A[m-1]:
                l = m + 1
            else:
                h = m - 1
        return -1

    def peakIndexInMountainArray_852_2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))

    def intersection_349(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            s = nums2
            l = nums1
        else:
            s = nums1
            l = nums2

        res = set()
        for v in s:
            if v in l:
                res.add(v)

        return [v for v in res]

    def intersection_349_2(self, nums1, nums2):

        nums2 = set(nums2)
        nums1 = set(nums1)

        return list(nums1.intersection(nums2))



x = [0,2,3, 1, 0]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
solver = Solution()

# print('peakIndexInMountainArray:', solver.peakIndexInMountainArray_852_2(x))
print('intersection_349:', solver.intersection_349_2(nums1, nums2))