class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        cnt = 0
        i = 0
        while i < len(nums):

            if nums[i - 1] == nums[i]:
                nums.remove(nums[i])
                i -= 1
            i += 1

        return nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solver = Solution()
print(solver.removeDuplicates(nums))
