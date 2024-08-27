# Link to the exercise : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

#Example 1:

#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.
#Example 2:

#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

#Constraints:

#1 <= haystack.length, needle.length <= 104
#haystack and needle consist of only lowercase English characters.

############### EXERCISE ###############
########################################

def indexFirstOcc(haystack, needle):
    ln = len(needle)
    lh = len(haystack)

    for i in range (0,lh):
        current_word = haystack[i:ln]
        if current_word == needle:
            return i
        ln += 1

    return -1

haystack = "bddfjdogkskk"
needle = "dog"
print(indexFirstOcc(haystack,needle))