# 🌳 **LeetCode 404 — Sum of Left Leaves**

'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

'''

# <---------------------------------------------------------->

'''
Another tree problem completed! 🚀

At first glance, this problem looks simple, but the interesting part is figuring out how to identify **whether a leaf belongs to the left side** while traversing the tree.

### 🧠 Thought Process

The key questions I asked myself:

➡️ What exactly makes a node a **leaf**?
➡️ How can I know whether the current node is a **left child**?
➡️ How can I carry that information during recursion?
➡️ What should happen when I reach a `None` node?
➡️ Once I find a valid left leaf, how should its value contribute to the final answer?

Breaking the problem into these smaller questions made the recursive approach much easier to understand.

### 🔍 Approach

• Traverse the binary tree using **DFS (Depth-First Search)**
• Keep track of whether the current node is a **left child**
• Identify leaf nodes during traversal
• Add a node's value only when it satisfies the required condition
• Combine the results from the left and right subtrees

### ⏱️ Complexity

**Time:** O(N) — each node is visited once.

**Space:** O(H) — recursion stack depends on the height of the tree.

### 💡 What I Learned

This problem reinforced an important tree-recursion idea:

> Sometimes the recursive function needs more information than just the current node.

Passing additional state such as **"is this a left child?"** can make the problem much easier to reason about.

One problem at a time. One concept at a time. 🌱

#LeetCode #DSA #Python #BinaryTree #Recursion #DFS #CodingJourney #100DaysOfCode #SoftwareEngineering #LearningInPublic

'''

# CODE: SOLUTIONS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        def dfs(node, isLeft):
            if not node: return 0

        # check karo leaf node hai ya nahi.
            if not node.left and not node.right:

                # left leaf hai to value return karo.
                return node.val if isLeft else 0

        # left child ke liye True pass kare
            left_node = dfs(node.left, True)

        # right child ke liye False pass kare.
            right_node = dfs(node.right, False)

        # Add both of left leaf chlid value
            return left_node + right_node

        return dfs(root, False)

        