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

    def twoSum_167(self, numbers, target):
        """

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1

        while i < m and j > 0:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

    def twoSum_167_2(self, numbers, target):
        """
        time limit exceeded
        """
        n = len(numbers)

        for i in range(n):
            temp = target - numbers[i]
            l = i + 1
            h = n - 1

            while l <= h:
                m = l + (h-1) // 2
                if numbers[m] == temp:
                    return [i+1, m+1]
                elif numbers[m] < temp:
                    l = m + 1
                else:
                    h = m - 1

    def intersect_350(self, nums1, nums2):
        """
        init
        faster without deciding short or long
        """
        # if len(nums1) < len(nums2):
        #     s = nums1
        #     l = nums2
        # else:
        #     l = nums1
        #     s = nums2

        res = []
        idx = []
        for ele in nums1:
            for i, ele2 in enumerate(nums2):
                if ele == ele2 and i not in idx:
                    res.append(ele)
                    idx.append(i)
                    break
        return res

    def intersect_350_2(self, nums1, nums2):
        """
        sorted
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        l = 0
        h = len(nums2) - 1

        res = []
        idx = []
        for ele in nums1:
            while l <= h:
                m = (l + h) // 2
                if nums2[m] == ele and m not in idx:
                    res.append(ele)
                    idx.append(m)
                    break
                elif m in idx:
                    m += 1
                if nums2[m] > ele:
                    h = m - 1
                elif nums2[m] < ele:
                    l = m + 1
        return res








x = [0,2,3, 1, 0]
nums1 = [1,2]
nums2 = [1,1]
numbers = [-1,0]
target = -1
solver = Solution()

# print('peakIndexInMountainArray:', solver.peakIndexInMountainArray_852_2(x))
# print('intersection_349:', solver.intersection_349_2(nums1, nums2))
# print('twoSum_167:', solver.twoSum_167_2(numbers, target))
# print('intersect_350:', solver.intersect_350(nums1, nums2))
print('intersect_350_2:', solver.intersect_350_2(nums1, nums2))