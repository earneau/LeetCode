# Link to the exercise : https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

############### EXERCISE ###############
########################################

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        answer = ""

        for i in range(0,len(ransomNote)):
            for j in range(0,len(magazine)):
                if ransomNote[i] == magazine[j]:
                    answer += ransomNote[i]
                    magazine = magazine.replace(ransomNote[i],"",1)
                    break
                
        if answer == ransomNote:
            return True
        
        return False
        