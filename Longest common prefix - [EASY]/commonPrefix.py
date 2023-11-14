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
    stop = False
    i = 0
    prefix = ""

    if len(strs) == 1:  # if there's only one word the common prefix is the whole word
        return strs[0]
    
    while stop == False:
        for word in strs:
            if word[:i] != prefix: 
                stop == True
                return prefix[:i-1] # this prefix doesnt work so the good one was the last one (hence [:i-1])
        i += 1
        prefix = strs[0][:i]

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))