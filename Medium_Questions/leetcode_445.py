# Add Two Numbers II — Using Stacks || 11ms
'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their 
nodes contains a single digit. Add the two numbers and return 
the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

 

Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?

'''


# CODE: SOLUTIONS: https://leetcode.com/problems/add-two-numbers-ii/solutions/8492369/add-two-numbers-ii-using-stacks-11ms-by-sh3vh



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    # Initialize two stacks to process the numbers from right to left
        stack1 = []
        stack2 = []

    # Traverse l1 and store each digit in stack1.
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

    # Traverse l2 and store each digit in stack2.
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

    ## Create a dummy node to build the result linked list.
        dummy = ListNode(-1)
        current = dummy
        carry = 0
    
    # Continue while there are digits left in either stack or a carry remains.
        while stack1 or stack2 or carry:
        # Get the rightmost digit from each stack. 
        # If a stack is empty, use 0.
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0

    # Add both digits along with the carry from the previous addition.
            val = v1 + v2 + carry
        # Calculate the carry for the next digit.
            carry = val // 10
        # Keep only the current digit.
            val = val % 10

            # Create a new node for the current digit.
            new_node = ListNode(val)
        # Insert the new node at the front of the result list.
            new_node.next = current.next
            current.next = new_node

    # Return the actual head of the result list.
        return dummy.next


