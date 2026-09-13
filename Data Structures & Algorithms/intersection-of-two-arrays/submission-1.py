class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = defaultdict(int)
        for num in nums1:
            hmap[num] = 1
        res = []
        for num in nums2:
            if hmap[num] == 1:
                hmap[num] = 0
                res.append(num)
        return res            
