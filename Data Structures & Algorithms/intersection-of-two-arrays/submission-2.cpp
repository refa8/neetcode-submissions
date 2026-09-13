class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> hmap;

        for (int num : nums1){
            hmap[num] = 1;
           
        }
            
        vector<int> res;
        for (int num : nums2){
            if (hmap[num] == 1){
                hmap[num] = 0;
                res.push_back(num);

            }
                

        }
            
        return res; 
    }
};