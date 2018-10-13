class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)

        if n == 0:
            return ''
        
        if n == 1:
            return strs[0]
        
        j = 0
        minlen = float('inf')
        
        while True:            
            for i in range(n):

                if strs[i] == '':
                    return ""

                if strs[0][j] != strs[i][j]:
                    return strs[0][0:j]

                if j == 0:
                    minlen = min(minlen, len(strs[i]))
        
            j += 1     
            if j == minlen:
                return strs[0][0:j]


strs = ["flow"]
solver = Solution()
print(solver.longestCommonPrefix(strs))