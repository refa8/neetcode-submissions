class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int carry = 1;
        int i = 0;
        reverse(digits.begin(),digits.end());
        while (carry){
            if (i<n){
                if (digits[i] == 9){
                    digits[i] = 0;
                }    
                else{
                    digits[i]+=1;
                    carry = 0;
                }    
            }        
            else{
                digits.push_back(1);
                carry = 0  ;
            }          
            i+=1;
        }    
        reverse(digits.begin(),digits.end());
        return digits;

    }
};
