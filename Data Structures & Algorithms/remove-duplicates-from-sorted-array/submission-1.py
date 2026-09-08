class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set(nums)
        nums[:len(unique)] = sorted(unique)
        return len(unique)
        