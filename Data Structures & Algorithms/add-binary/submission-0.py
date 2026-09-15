class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a, b = a[::-1], b[::-1]
        res = ""
        for i in range(max(len(a),len(b))):
            A = int(a[i]) if i < len(a) else 0
            B = int(b[i]) if i < len(b) else 0
            total = (A + B + carry)
            ans = str(total%2)
            res = ans + res
            carry = total//2
        
        if carry:
            res= "1"+ res          

        



        return res   
        