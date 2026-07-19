class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!= t.length()){
            return false; 
        }

        // map all letters to an alpha array
        int[] counts = new int[26];

        for(int i = 0; i < s.length(); i++){
            int s_index = s.charAt(i); 
            int t_index = t.charAt(i); 
            counts[s_index - 'a']++; 
            counts[t_index - 'a']--; 
        }

        // they should all be 0 
        for(int i : counts){
            if(i != 0) return false; 
        }
        return true; 

        

    }
}
