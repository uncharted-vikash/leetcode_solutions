# 🧠 Cracking Code Patterns: The Simple Logic Behind BST Insertions 👇

'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.

'''



# <----------------------------------------------------------------------------->


# 💡 The Intuition:

# The beauty of a BST is its inherent order. When inserting a new value, we don't need to reorganize the entire tree. We just need to search for the correct empty spot (a None pointer) where the value logically belongs.

# Instead of using recursion—which adds overhead to the call stack—we can use a simple while True loop to drift down the tree until we find an open slot.

# 🛠️ The Tactical Approach

# 1. Handle the Base Case: If the tree is completely empty (root is None), the new node becomes the root. 

# 2.Traverse the Tree: Use a pointer (current) to navigate.

# 3. Make the Decision:

#     1. If the target value is less than the current node's value, check the left child. 
#     2. If it’s empty, insert the node and break. Otherwise, move left.If the target value is greater, check the right child. If it’s empty, insert the node and break. Otherwise, move right.
    
#     4. Return the Root: Return the original root of the modified tree.

# 📊 Complexity AnalysisTime 
#     Complexity: O(H), where H is the height of the tree. In the best/average case (balanced tree), this takes \(O(\log N)\) time. In the worst case (skewed tree/linked list shape), it takes O(N) time.
    
#     Space Complexity: O(1) Auxiliary Space! Because we used an iterative pointer approach instead of recursion, we don't use any extra space on the call stack.Here is the clean Python implementation:



# CODE: SOLUTIONS:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
    # if empty node, then return new node
        if not root: return TreeNode(val)

        current = root
    # Traverse, when we not find the best position for the node.
        while True:
            # if val less then current.val go left , if left is not none.
            # otherwise we find best position for new node
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left

            else:
            # if val greater then current.val go right , if right is not none.
            # otherwise we find best position for new node
                if not current.right:
                    current.right = TreeNode(val)
                    break

                current = current.right

        return root
    
