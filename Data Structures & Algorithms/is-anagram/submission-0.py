class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sNew = sorted(s)
        tNew = sorted(t)
        if sNew != tNew:
            return False
        return True                  

            

        