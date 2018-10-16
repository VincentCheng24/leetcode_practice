import numpy as np


class Solution:
    def searchInsert_35(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        h = len(nums)-1
        l = 0
        while l < h:
            m = (l + h) // 2
            if nums[m] == target:
                return m

            elif nums[m] > target:
                h = m - 1

            else:
                l = m + 1

        if nums[l] < target: # now nums[l] is the cloest num, so check it is enough
            l += 1
        return l

    def maxSubArray_53(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        mx = - np.inf

        for ele in nums:
            max_so_far += ele

            if max_so_far > mx:
                mx = max_so_far
            if max_so_far < 0:
                max_so_far = 0

        return mx

    def maxSubArray_53_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)

    def plusOne_66(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne_66(digits[0:-1]) + [0]

    def plusOne_66_2(self, digits):
        s = ''.join(map(str, digits))
        i = int(s) + 1
        return [int(x) for x in str(i)]

    def plusOne_66_3(self, digits):
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        if digits[0] == 0:
            return [1] + digits

    def merge_sorted_array_88(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        for i in range(m, m+n):
            cur_idx = i
            cur_val = nums1[i]
            while cur_idx > 0 and nums1[cur_idx-1] > cur_val:
                nums1[cur_idx] = nums1[cur_idx-1]
                cur_idx -= 1
            nums1[cur_idx] = cur_val
        return nums1

    def merge_sorted_array_88_2(self, nums1, m, nums2, n):

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        return nums1

    def generate_Pascal_Triangle_118(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        i = 1
        while i <= numRows:
            row = [1] * i
            if i > 2:
                for idx in range(1, i-1):
                    p_row = res[i-1-1]
                    row[idx] = p_row[idx-1] + p_row[idx]

            res.append(row)
            i += 1
        return res

    def generate_Pascal_Triangle_II_119(self, rowIndex):

        if rowIndex < 2:
            return [1] * (rowIndex+1)
        else:
            p_row = [1, 1]
            i = 3
            while i <= rowIndex + 1:
                row = [1] * i
                if i > 2:
                    for idx in range(1, i - 1):
                        row[idx] = p_row[idx - 1] + p_row[idx]

                p_row = row
                i += 1
            return p_row

    def Best_Time_to_Buy_and_Sell_Stock_121(self,prices):

        mx = 0
        mn_sofar = 1000
        for i in range(len(prices)):
            mn_sofar = min(mn_sofar, prices[i])
            mx = max(mx, prices[i]-mn_sofar)
        return mx

    def sortArrayByParity_905(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[j], A[i] = A[i], A[j]
                j += 1
        return A

    def checkPossibility_665(self, nums):
        """
        an initial solution
        """
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                j = 2
                while i+j < len(nums) and nums[i] > nums[i+j] and i-1 >= 0 and nums[i-1] > nums[i+1]:
                    cnt += 1
                    j += 1
            if cnt > 1:
                return False
        return True


    def checkPossibility_665_2(self, nums):
        """
        a brilliant solution but it's more expensive
        """
        opt_one = nums[:]
        opt_two = nums[:]

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                opt_one[i] = nums[i+1]
                opt_two[i+1] = nums[i]
                break

        return opt_one == sorted(opt_one) or opt_two == sorted(opt_two)

    def rotate_189(self, nums, k):
        """
        init
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp

        return nums

    def rotate_189_2(self, nums, k):
        '''
        using reverse
        '''

        k %= len(nums)
        nums[-k:] = reversed(nums[-k:])
        nums[:-k] = reversed(nums[:-k])
        nums.reverse()

        return nums

    def thirdMax_414(self, nums):
        'init'

        th_max = -float("inf")
        sc_max = -float("inf")
        fi_max = -float("inf")

        for v in nums:
            if v > fi_max:
                th_max = sc_max
                sc_max = fi_max
                fi_max = v
            elif v > sc_max and v != fi_max:
                th_max = sc_max
                sc_max = v
            elif v > th_max and v != sc_max and v != fi_max:
                th_max = v

        if th_max != -float("inf"):
            return th_max
        else:
            return fi_max










nums1 = [1,2,2,5,3,5]
m = 3
nums2 = [2,3,3,2,4]
n = 3

solver = Solution()

# print(solver.searchInsert(lis, t))
# print(solver.maxSubArray_53_2(lis))
# print(solver.plusOne_66(lis))
# print(solver.merge_sorted_array_88(nums1, m, nums2, n))
# print(solver.generate_Pascal_Triangle_118(4))
# print(solver.sortArrayByParity_905(nums1))
# print(solver.checkPossibility_665_2(nums2))
# print(solver.rotate_189_2(nums1, 1))
print(solver.thirdMax_414(nums1))
# print(solver.searchInsert(lis, t))
