# Link to the exercise : https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

############ INSTRUCTIONS ##############
########################################

# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.

############### EXERCISE ###############
########################################

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = [] # result string from which we'll use the length
        current = ""
        i = 0       # setting up counter

        while i < len(s):
            if s[i] not in current:
                current += s[i]
            else:
                result.append(current)  # chain breaks, append and reset current string
                current = "" + s[i]     # current string now starts with the current character
            
            i += 1

        result.append(current)  # when the while finishes the last current is not appended so it needs to be done here
        return len(result)