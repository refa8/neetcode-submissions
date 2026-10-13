class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        start= 0
        wdw =0
        for end in range(len(s)):
            
            if s[end] in indices:
                start = max(indices[s[end]]+1,start)
            indices[s[end]]= end
            wdw=max(wdw,end-start+1)    
                 
               
            
            
            
        return wdw

            

        