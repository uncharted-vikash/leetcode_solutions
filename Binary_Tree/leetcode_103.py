# 🔄 Zigzag Level Order Traversal | BFS + Alternate Level Reversal

'''
Given the root of a binary tree, return the zigzag level order traversal of 
its nodes' values. (i.e., from left to right, then right to left for the 
next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

'''



'''
# 🔄 Zigzag Level Order Traversal | BFS + Alternate Level Reversal

## 💡 Intuition

A normal level-order traversal visits a binary tree **level by level from left to right**.

For zigzag traversal, we simply alternate the direction:

* Level 0 → Left → Right
* Level 1 → Right → Left
* Level 2 → Left → Right
* Level 3 → Right → Left

We can achieve this efficiently using **BFS with a queue**. After collecting each level from left to right, we reverse the values of every alternate level.

## 🚀 Approach

1. If the tree is empty, return an empty list.
2. Use a `deque` to perform **Breadth-First Search (BFS)**.
3. For each level:

   * Store the current number of nodes using `level_size`.
   * Remove exactly `level_size` nodes from the queue.
   * Add their values to `curr_level_value`.
   * Add their left and right children to the queue.
4. If the current level should be traversed from right to left, reverse the collected values.
5. Add the current level to the final result.
6. Continue until the queue becomes empty.

## ⏱️ Complexity

**Time Complexity:** `O(N)`

Each node is visited exactly once. Reversing each level also takes time proportional to the number of nodes in that level, so the total remains `O(N)`.

**Space Complexity:** `O(N)`

The queue and the result can hold up to `O(N)` elements in the worst case.

## 🎯 Key Takeaway

Use **BFS for level-by-level traversal**, and simply **reverse every alternate level** to achieve the zigzag pattern.

'''


# CODE; SOLUTIONS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:    # if tree is empty then return empty list
            return []

        q = deque([root])
        result = []
    # processing while queue is not empty
        while q:
            level_size = len(q)
            curr_level = []

        # Process all nodes of the current level
            for _ in range(level_size):
                node = q.popleft()
                
                # Add current node's value to the current level
                curr_level.append(node.val)

                # Add left child for the next level
                if node.left:
                    q.append(node.left)

                # Add right child for the next level
                if node.right:
                    q.append(node.right)

            # Reverse every alternate level to create zigzag order
            # if len result is odd then reverse(right -> left) otherwise not 
            curr_level = curr_level[::-1] if len(result) % 2 else curr_level

            result.append(curr_level)


        return result

