# Link to the exercise : https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

############### EXERCISE ###############
########################################

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            midpoint = (begin + end)//2
            midpoint_value = nums[midpoint]

            if midpoint_value == target:
                return midpoint

            elif midpoint_value >= nums[begin]:
                if (target < midpoint_value and target >= nums[begin]):
                    end = midpoint - 1
                else:
                    begin = midpoint + 1
            
            else:
                if (target > midpoint_value and target <= nums[end]):
                    begin = midpoint + 1
                else:
                    end = midpoint - 1
        return -1