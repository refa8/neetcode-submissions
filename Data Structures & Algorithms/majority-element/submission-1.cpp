class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int ,int> count;
        int res = 0;
        int maxCount = 0;
        for(int num : nums){
            count[num] += 1;
            if (count[num] > maxCount){
                maxCount = count[num];
                res = num;

            }
                

        }
            
        return res;         
                

        
        
    }
};