class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        i = 0
        digits.reverse()
        while carry:
            if i<n:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i]+=1
                    carry = 0
            else:
                digits.append(1)
                carry = 0        
            i+=1
        digits.reverse()  
        return digits  
