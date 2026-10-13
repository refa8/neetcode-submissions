class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum=[0]*(n+1)
        for i in range(n):
            
            prefixSum[i+1]=nums[i]+prefixSum[i]

        for i in range(1,len(prefixSum)):
            if prefixSum[i-1]==prefixSum[len(prefixSum)-1]-prefixSum[i]:
                return i-1
        return -1