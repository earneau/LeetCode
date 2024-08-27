# Link to the exercise : https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

#Example 1:

#Input: nums = [3,2,3]
#Output: 3
#Example 2:

#Input: nums = [2,2,1,1,1,2,2]
#Output: 2
 

#Constraints:

#n == nums.length
#1 <= n <= 5 * 104
#-109 <= nums[i] <= 109
 

#Follow-up: Could you solve the problem in linear time and in O(1) space?

############### EXERCISE ###############
########################################

# the idea is that once sorted, the majority element of the array will always be at n/2 indice

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    l = len(nums)
    return nums[l/2]
            
nums = [2,3,2,3,4,3]
result = majorityElement(nums)
print(result)