class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = [0]*n
        for i in range(n):
            pos = (i+k)%n
            temp[pos] = nums[i]
        for i in range(n):
            nums[i] = temp[i]    
        