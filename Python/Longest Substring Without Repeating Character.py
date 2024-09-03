# Link to the exercise : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given a string s, find the length of the longest substring without repeating characters.

############### EXERCISE ###############
########################################

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0    
        current_string = ""
        
        max_length = 0    
        dictionary = {}

        while j < len(s):  
            if s[j] not in current_string:
                dictionary[s[j]] = j
                current_string = current_string + s[j]
                max_length = max(max_length, len(current_string))
            else:
                i = dictionary.get(s[j])
                dictionary[s[j]] = j
                current_string = s[i:j]
            j += 1

        return max_length