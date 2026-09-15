class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1

        for i in range(n):
            freq[nums[i]]-=1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                freq[nums[j]]-=1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1,n):
                    freq[nums[k]]-=1
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    fourth = target-nums[k]-nums[j]-nums[i] 
                    if freq[fourth]>0:
                        res.append([nums[i],nums[j],nums[k],fourth])

                for k in range(j+1,n):
                    freq[nums[k]]+=1
            for j in range(i+1,n):
                freq[nums[j]]+=1
        return res                  


                    