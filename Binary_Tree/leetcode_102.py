# 102. Binary Tree Level Order Traversal
'''
Given the root of a binary tree, return the 
level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''



'''
Intuition
Level Order Traversal means visiting the nodes level by level from left to right.

A Queue is ideal for this because it follows FIFO (First In, First Out). We first process the parent nodes, then add their children to the queue for the next level.

To separate nodes belonging to different levels, we store the current queue size in level_size. This tells us exactly how many nodes belong to the current level.

Approach
1. If root is None, return an empty list.
2. Initialize a queue and add the root node.
3. While the queue is not empty:
    -> Store the current queue size as level_size.
    -> Create a list curr_ans for the current level.
    -> Process exactly level_size nodes:
        -> Remove a node from the front of the queue.
        -> Add its value to curr_ans.
        -> Add its left child to the queue if it exists.
        -> Add its right child to the queue if it exists.
        -> Add curr_ans to the final result.
4. Return the result.

Complexity
    Time Complexity: O(n) — every node is visited exactly once.
    Space Complexity: O(w) — where w is the maximum width of the tree.

'''

# CODE: SOLUTIONS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # Time: O(N) || Space: O(W) , w is width of binary tree

    # if the tree is empty, return an empty list
        if not root:
            return []

    # Intialize a list for storing level values
        result = []

    # Queue is used for BFS Traversal.
        q = deque([root])

    # proccess while all node have been processed.
        while q:
        # Number of nodes currently present at this level.
            level_size = len(q)

            # to store current level values
            curr_ans = []

        # Process exactly all node present curent level
            for _ in range(level_size):
            # remove front node of the deque
                e = q.popleft()

            # Add the current node value to the curr_ans 
                curr_ans.append(e.val)

            # Add the left tree for processing in the next level
                if e.left:
                    q.append(e.left)

            # Add the left tree for processing in the next level
                if e.right:
                    q.append(e.right)

        #  Add the complete level to the final result
            result.append(curr_ans)

        # return all levels
        return result
