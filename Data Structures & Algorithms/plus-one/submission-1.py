class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return [1]
            
        if digits[-1] < 9:
            digits[-1]+=1
            return digits

        digits = self.plusOne(digits[:-1])
        digits.append(0)
        return digits
            

                
        