# Link to the exercise : https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

############ INSTRUCTIONS ##############
########################################

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

############### EXERCISE ###############
########################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        pos = 0
        longer = 0
        ans = ""
        if len(word1) < len(word2):
            pos = len(word1)
            longer = 2
        else:
            pos = len(word2)
            longer = 1

        for i in range (pos):
            ans = ans + word1[i]
            ans = ans + word2[i]

        if longer == 1:
            ans = ans + word1[pos:]
        elif longer == 2:
            ans = ans + word2[pos:]
        
        return ans