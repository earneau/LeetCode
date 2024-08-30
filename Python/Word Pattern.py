# Link to the exercise : https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

############### EXERCISE ###############
########################################

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        dictionary = {}

        words = list(s.split(" "))

        if len(words) != len(pattern):
            return False
        
        for i in range(0,len(pattern)):
            print(pattern[i])
            if (pattern[i] in dictionary.keys()) or (words[i] in dictionary.values()):
                print(words[i])
                
                print(dictionary.get(pattern[i]))
                if words[i] != dictionary.get(pattern[i]):
                    return False
            else:
                dictionary[pattern[i]] = words[i]

        return True