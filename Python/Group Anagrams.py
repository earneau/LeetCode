# Link to the exercise : https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

############### EXERCISE ###############
########################################

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}

        for word in strs:
            tri = "".join(sorted(word))
            if tri in dictionary.keys():
                dictionary[tri].append(word)
            else:
                dictionary[tri] = [word]
        
        answer = []

        for lists in dictionary.values():
            answer.append(lists)

        return answer