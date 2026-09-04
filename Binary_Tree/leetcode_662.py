# Binary Tree Width | BFS + Complete Binary Tree Indexing | O(N)

'''
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

'''

'''
Intuition :-
Think of the binary tree as if it were a complete binary tree.

Even when some nodes are missing, we assign every node the index it would have in a complete binary tree:

    Left child → 2 * index + 1
    Right child → 2 * index + 2
    For every level, the width is:

last_index - first_index + 1

This automatically counts the gaps between nodes, which is exactly what the problem requires.

We use BFS (Level Order Traversal) so that we can process one level at a time.

Approach :-
    If root is None, return 0.
    Use a queue to store (node, index).
    Start with (root, 0).
    For each level:
        Get the index of the first node.
        Get the index of the last node.
        Calculate:
        width = last_index - first_index + 1
        Update max_width.
    Add children to the queue using complete-tree indexing:
        Left → 2 * index + 1
        Right → 2 * index + 2
    Return the maximum width.

Complexity
    Time: O(N) — every node is processed once.
    Space: O(N) — the queue can contain up to N nodes in the worst case.
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
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
    # if tree has no node then return 0
        if not root:
            return 0
    # we store node and index
        q = deque([(root, 0)])
        max_width = 0
    # Process the tree level by level
        while q:
            level_size = len(q)
        # extract first and last index from deque 
            first_index = q[0][1]
            last_index = q[-1][1]

            curr_width = last_index - first_index + 1
        # calculate max_width 
            max_width = max(max_width, curr_width)

        # processing every node in the  current level 
            for _ in range(level_size):
                node, index = q.popleft()

            # Assign index to the left child
                if node.left:
                    q.append((node.left, 2*index+1))

            # Assign index to the right child
                if node.right:
                    q.append((node.right, 2*index+2))

        return max_width


