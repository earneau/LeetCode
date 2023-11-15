############ INSTRUCTIONS ##############
########################################

#Given a string s consisting of words and spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.

 

#Example 1:

#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.
#Example 2:

#Input: s = "   fly me   to   the moon  "
#Output: 4
#Explanation: The last word is "moon" with length 4.
#Example 3:

#Input: s = "luffy is still joyboy"
#Output: 6
#Explanation: The last word is "joyboy" with length 6.
 

#Constraints:

#1 <= s.length <= 104
#s consists of only English letters and spaces ' '.
#There will be at least one word in s.

############### EXERCISE ###############
########################################

# using the split function allows us to get a list of all the words in their natural order, excluding all the spaces
# we can then pick up the last words of our newly found split list and return its length

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    split = s.split()
    l = len(split)
    return len(split[l-1])

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
