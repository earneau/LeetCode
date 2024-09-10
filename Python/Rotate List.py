# Link to the exercise : https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given the head of a linked list, rotate the list to the right by k places.

############### EXERCISE ###############
########################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        
        last.next = head    # make the list circular
        
        k = k % length # find the new tail (length - k % length - 1) 
        new_tail_position = length - k - 1 # and new head (length - k % length)
        new_tail = head
        
        for _ in range(new_tail_position):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None # break the circular link
        return new_head