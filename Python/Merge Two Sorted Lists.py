# Link to the exercise : https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

############### EXERCISE ###############
########################################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(None)
        answer = dummy

        while list1 != None or list2 != None:
            val1 = list1.val if list1 is not None else (list2.val + 1)
            val2 = list2.val if list2 is not None else (list1.val + 1)

            if val1 <= val2:
                new = ListNode(val1)
                list1 = list1.next if list1 is not None else None
            elif val2 < val1:
                new = ListNode(val2)
                list2 = list2.next if list2 is not None else None

            answer.next = new
            answer = answer.next
        
        return dummy.next