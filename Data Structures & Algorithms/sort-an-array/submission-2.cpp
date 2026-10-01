class Solution {
public:
    

    void mergeSort(vector<int>& arr,int l,int r){
        if (l>=r){
            return;
 
        }
             
        int m = (l+r)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);

    }
         


    void merge(vector<int>&arr,int L, int M, int R){
        vector<int>left(arr.begin()+L,arr.begin()+M+1);
        vector<int>right(arr.begin()+M+1,arr.begin()+R+1);
        int i = L;
        int l = 0;
        int r = 0;
        while(l<left.size() && r<right.size()){
            if (left[l] <= right[r]){
                arr[i] = left[l];
                l+=1;

            }
                
            else{
                arr[i] = right[r];
                r+=1;

            }
                
            i+=1;
        }
            
        while (l<left.size()){
            arr[i] = left[l];
            l+=1;
            i+=1;

        }
            

        while (r<right.size()){
            arr[i] = right[r];
            r+=1;
            i+=1;

        }
                

    }

    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums,0,nums.size()-1);
        return nums;

    }
            

     

           
};