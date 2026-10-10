class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1

        for i in range(len(nums)):
            if nums[i]>0:
                break

            freq[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                freq[nums[j]]-=1
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                third=-(nums[i]+nums[j])
                if freq[third]>0:
                    res.append([nums[i],nums[j],third])
            for j in range(i+1,len(nums)):
                freq[nums[j]]+=1        

        return res            

            



        