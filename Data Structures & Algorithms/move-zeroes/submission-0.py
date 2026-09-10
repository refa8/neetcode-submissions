class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        temp = []
        for num in nums:
            if num != 0:
                temp.append(num)

        temp1 = sorted(temp)
        for i in range(len(nums)):
            if i < len(temp1):
                nums[i] = temp[i]
            else:
                nums[i] = 0
        
        
                        



        