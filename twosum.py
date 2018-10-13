class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
		
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if ((nums[i] + nums[j] == target) & (i < j) ):
					return [i,j] 

                
list_a = [3,2,2,4]
target = 6
test = Solution()
print test.twoSum(list_a, target)

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#		return [[i,j] for i in range(0, len(nums)-1) for j in range(0, len(nums)-1) if ((nums[i] + nums[j] == target) & (i < j))]