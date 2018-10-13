class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        len_nums = len(nums)
        t = 0
        for i in range(len_nums):
		    for j in range(i,len_nums):
			    for m in range(j,len_nums):
				    if nums[i] + nums[j] + nums[m] == 0:
					    t += 1
						res[t] = [i,j,m]
                        
	
	return res
	

nums = [-1,0,1,2,-1,-4]
sol = Solution()
print sol.threeSum(nums)