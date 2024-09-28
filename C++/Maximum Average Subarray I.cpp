// Link to the exercise : https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

// INSTRUCTIONS //

// You are given an integer array nums consisting of n elements, and an integer k.
// Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

// EXERCISE //

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();  

        double windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        double maxAverage = windowSum / k;  

        for (int i = k; i < n; i++) {
            windowSum += nums[i] - nums[i - k];
            maxAverage = max(maxAverage, windowSum / k);  
        }

        return maxAverage;
    }
};

