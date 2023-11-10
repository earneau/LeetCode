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

# this solution seems to work on my IDE but isnt validated on Leetcode

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    for i in range (0, l):
        cpt = 1
        for j in range (i + 1,l):
            print(nums[j])
            if nums[i] == nums[j]:
                cpt += 1
            if cpt >= l/2:
                return nums[i]
            
nums = [2,3,2,3,4,3]
result = majorityElement(nums)
print(result)