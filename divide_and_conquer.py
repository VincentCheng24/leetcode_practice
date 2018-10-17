class Solution:
    def majorityElement_169_1(self, nums):
        """
        an init
        :type nums: List[int]
        :rtype: int
        """
        cnt = dict()

        for v in nums:
            if v not in cnt:
                cnt[v] = 0
            cnt[v] += 1

            if cnt[v] > len(nums) // 2:
                return v

    def majorityElement_169_2(self, nums):
        """
        a more concise one
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(nums)
        return sorted(nums)[len(nums) // 2]

    def maxSubArray_53_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)

    def maxSubArray_53_2(self,A):
        ans = A[0]
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            ans = max(sum,ans)
            sum = max(sum,0)

        return ans

    def findKthLargest_215(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)

        return nums[-k]

    def findKthLargest_215_2(self, nums, k):
        """
        a DC solution
        """
        j = 0
        max_idx = []
        while j < k:
            mx = -float('inf')
            idx = -1
            for i in range(len(nums)):
                if nums[i] > mx and i not in max_idx:
                    mx = nums[i]
                    idx = i
            max_idx.append(idx)
            j += 1
        return mx



x = [3,2,1,5,6,4]
k = 5

solver = Solution()

# print('findKthLargest_215 :', solver.findKthLargest_215(x, k))
print('findKthLargest_215_2 :', solver.findKthLargest_215_2(x, k))