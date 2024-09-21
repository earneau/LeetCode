// Link to the exercise : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

// INSTRUCTIONS //

// There are n kids with candies. You are given an integer array candies, 
// where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 
// denoting the number of extra candies that you have.

// Return a boolean array result of length n, where result[i] is true if, 
// after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, 
// or false otherwise.

// Note that multiple kids can have the greatest number of candies.

// EXERCISE //

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = *max_element(candies.begin(), candies.end());
        vector<bool> result;
        
        for (int candy : candies) {
            result.push_back(candy + extraCandies >= maxCandies);
        }
        
        return result;
    }
};
