class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> count(3);
        for(int& num:nums){
            count[num]+=1;
        }
        int index = 0;
        for(int i =0;i<3;i++){
            while(count[i]){
                count[i]-=1;
                nums[index]=i;
                index+=1;
            }
        }
    }
};