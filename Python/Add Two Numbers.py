# Link to the exercise : https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

############### EXERCISE ###############
########################################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)     # dummy head, have the rest of the list next
        answer = dummy      # reference at the beginning of the ll
        retenue = 0

        while l1 != None or l2 != None or retenue != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            current_sum = val1 + val2 + retenue
            val = current_sum % 10
            retenue = current_sum // 10

            new = ListNode(val)

            answer.next = new
            answer = answer.next

            l1 = l1.next if l1 is not None else None   # move forward in the lists
            l2 = l2.next if l2 is not None else None
        
        
        return dummy.next
        