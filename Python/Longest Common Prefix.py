# Link to the exercise : https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

 

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
 

#Constraints:

#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters.

############### EXERCISE ###############
########################################

# this seems to work but isnt validated by leetwork
# test doesnt pass for strings such as ["",""] 

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
            return ""
    
    prefix = strs[0]

    for word in strs[1:]:
        while word.find(prefix) != 0:       # finds the first occurence of the prefix, returns -1 if the value isnt found
            prefix = prefix[:-1]
            if not prefix:
                return ""
            
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))