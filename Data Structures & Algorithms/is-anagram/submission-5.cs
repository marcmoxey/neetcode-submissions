public class Solution {
    public bool IsAnagram(string s, string t) {
        
        // check the length 
        if(s.Length != t.Length) {
            return false;
        }

        Dictionary<char, int> countS = new Dictionary<char, int>();
        Dictionary<char, int> countT = new Dictionary<char, int>();

        // get count 
        for(int i = 0; i < s.Length; i++) {
            // if key exists add 1, if not start at 0 then add 1
            countS[s[i]] = countS.GetValueOrDefault(s[i], 0) + 1;
            countT[t[i]] = countT.GetValueOrDefault(t[i], 0) + 1;
        }
        // checks both dictionaries have the same number of unique characters. 
            // and htere is nothing in countS that isn't also in countT
        return countS.Count == countT.Count && !countS.Except(countT).Any();
    }
}
