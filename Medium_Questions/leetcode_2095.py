# LeetCode 2095 — Delete the Middle Node:

'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105

'''



'''
Intuition:
Linked list mein humein middle node delete karni hai, lekin 
singly linked list mein kisi node ko delete karne ke liye uske previous node ki zarurat hoti hai.

Isliye dummy node + slow/fast pointers use karenge.

-> slow → 1 step
-> fast → 2 steps
-> fast ko slow se thoda aage se start karenge, taaki loop ke end par slow middle ke previous node par ho.
-> Then: slow.next = slow.next.next

Approach:
-> dummy node banao aur dummy.next = head.
-> slow = dummy, fast = head.
-> fast ko 2 steps aur slow ko 1 step move karo.
-> Jab fast end ke paas pahunch jaye, slow middle ke previous node par hoga.
-> slow.next ko skip karo.
-> dummy.next return karo.

complexity:
    Time: O(n)
    Space: O(1)

'''

# CODE: SOLUTION

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(23)
node2 = ListNode(45)
node3 = ListNode(63)
node4 = ListNode(87)
node5 = ListNode(38)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# current = head
# while current:
#     print(current.val, end=" ")
#     current = current.next



class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return None

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

            assert slow is not None

        # Delete middle node
        assert slow.next is not None
        slow.next = slow.next.next

        return head

delete_node = Solution()
delete_node.deleteMiddle(head)

current = head
while current:
    print(current.val, end=" ")
    current = current.next

