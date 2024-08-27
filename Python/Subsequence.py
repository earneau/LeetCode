# Link to the exercise : https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

#Example 1:

#Input: s = "abc", t = "ahbgdc"
#Output: true
#Example 2:

#Input: s = "axc", t = "ahbgdc"
#Output: false
 

#Constraints:

#0 <= s.length <= 100
#0 <= t.length <= 104
#s and t consist only of lowercase English letters.

############### EXERCISE ###############
########################################

def isSubsequence(s,t):
        cpt = 0

        if len(s) < 1:
            return True

        for i in range(0,len(t)):
            if t[i] == s[cpt]:
                cpt += 1
            if cpt >= len(s):
                return True
        return False  