public class Solution {
    public bool hasDuplicate(int[] nums) {
    //     // loop through array 
    //     for(int i = 0; i < nums.Length; i++)
    //     {
    //        for(int j = i + 1; j < nums.Length; j++) 
    //        {
    //             if(nums[i] == nums[j]) {
    //                 return true;
    //             }
    //        }
    //     }
    //     return false;

        // sort array 
        // Array.Sort(nums);

        // // loop through array 
        // for(int i = 0; i < nums.Length; i++ ) {
        //     // checking for dupes 
        //     if(nums[i] == nums[i-1]) 
        //     {
        //     return true;
        //     }

        // }

        // return false; 

        HashSet<int> newNums = new(); 

        foreach(var num in nums) 
        {
            if(newNums.Contains(num)) 
            {
                 return true;
            }
            newNums.Add(num);
        }
         
         return false;
    }
 }
