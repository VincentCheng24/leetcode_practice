import math

class Solution:
    def findDuplicates_442(self, nums):
        """
        naive solution
        """
        res = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    res.append(nums[j])
                    break
                j += 1
        return res

    def findDuplicates_442_sort(self, nums):
        """
        sort
        """
        res = []
        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])

        return res

    def findDuplicates_442_sort_set(self, nums):
        """
        sort & set
        """
        # nums = sorted(nums)
        snums = list(set(nums))
        for val in snums:
            nums.remove(val)
        return nums

        # print('well done')

    def findDuplicates_442_hash(self, nums):
        """
        some trick
        The idea is we do a linear pass using the input array itself as
        a hash table to store which numbers have been seen before.
        """
        res = []
        # nums = sorted(nums)
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]

        return res











solver = Solution()
nums = [2,2]

# print('findDuplicates:', solver.findDuplicates_442(nums))
# print('findDuplicates:', solver.findDuplicates_442_sort(nums))
# print('findDuplicates:', solver.findDuplicates_442_sort_set(nums))
print('findDuplicates:', solver.findDuplicates_442_hash(nums))