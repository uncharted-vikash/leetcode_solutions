# 🌳 Cracked LeetCode 124 — Binary Tree Maximum Path Sum!

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''

#   <----------------------------------------------------------------------->

'''
One of those problems that looks scary, but falls apart beautifully once you get the trick. Let me break it down 👇

🔍 The Intuition
A path can bend at exactly one node — it enters from one side and exits from the other.
So at every node, only two questions matter:

Is the best path ending at this node (one-armed)?
Is the best path bending at this node (left + node + right)?
The answer to Q2 can never go upward — so it's a candidate for the final answer, nothing more.
⚙️ The Approach (Post-order DFS)

At each node:
🔹 Get best sum from left & right subtrees (ignore negative sides → max(0, ...))
🔹 Update global max with the bent path (left + node + right)
🔹 Return only the one-armed path (node + better side) so the parent can extend it

Complexity
Metric	Value	Why
⏰ Time	O(N)	Har node sirf ek baar visit hoti hai
💾 Space	O(H)	Recursion stack — H = tree ki height

'''

# CODE: SOLUTIONS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int | float:
        # yeh variable poore tree ka sabse best path sum store karega
        self.max_sum = float('-inf')

        def dfs(node: TreeNode | None) -> int:
            # agar node None hai toh sum 0 hai, simple
            if not node:
                return 0

            # left aur right subtree se best sum nikalo
            # agar koi side negative de rahi hai, toh usse ignore karo (0 use karo)
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            # is node ke through full path: left + node + right
            # agar yeh ab tak ka best hai toh save kar lo
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)

            # parent ko wapas best "ek side" ka sum do
            # kyunki parent ke liye left OR right, dono nahi le sakte
            return node.val + max(left_sum, right_sum)

        dfs(root)

        return self.max_sum
        
    
        