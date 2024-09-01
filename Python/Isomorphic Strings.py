# Link to the exercise : https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

############### EXERCISE ###############
########################################

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for i in range(0,len(s)):
            if s[i] in dict_s and t[i] not in dict_t:
                return False
            if s[i] not in dict_s and t[i] in dict_t:
                return False

            if s[i] not in dict_s and t[i] not in dict_t:
                dict_s[s[i]] = i
                dict_t[t[i]] = i
            else:       
                if dict_s[s[i]] != dict_t[t[i]]:
                    return False
                dict_s[s[i]] = i
                dict_t[t[i]] = i
        
        return True