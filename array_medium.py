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











solver = Solution()
nums = [4,3,2,7,8,2,3,1,8]

# print('findDuplicates:', solver.findDuplicates_442(nums))
# print('findDuplicates:', solver.findDuplicates_442_sort(nums))
print('findDuplicates:', solver.findDuplicates_442_sort_set(nums))