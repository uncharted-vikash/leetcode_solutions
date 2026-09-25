'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

'''
# <------------------------------------------------------------->

'''
🌳 **Validate Binary Search Tree — Think Beyond the Parent!**

### 🧠 Intuition

A Binary Search Tree follows one important rule:

**Every node in the left subtree must be smaller, and every node in the right subtree must be greater than the current node.**

But here’s the tricky part 👇

It’s **not enough to compare a node only with its parent**.

A node can be smaller than its parent but still violate a restriction created by an ancestor.

💡 **Key idea:**
Instead of checking only the parent, carry a valid **range `(low, high)`** for every node.

---

### 🚀 Approach

Start with the entire possible range:

**(-∞, +∞)**

For every node:

1. Check whether its value lies inside the current valid range.
2. For the **left subtree**, update the upper limit to the current node.
3. For the **right subtree**, update the lower limit to the current node.
4. If any node falls outside its allowed range → **Invalid BST ❌**
5. If every node satisfies its range → **Valid BST ✅**

This turns the BST property into a simple **range-validation problem**.

---

### ⏱️ Complexity

**Time:** `O(N)`
Every node is visited at most once.

**Space:** `O(H)`
Where `H` is the height of the tree because of the recursion stack.

* Balanced tree → `O(log N)`
* Skewed tree → `O(N)`

---

🔥 **Interview Insight**

When validating a BST, don't think:

> “Is this node smaller/larger than its parent?”

Think:

> **“What values are allowed at this position in the tree?”**

That shift in thinking makes the solution much easier to derive in an interview.

#LeetCode #DSA #BinaryTree #BST #Python #CodingInterview #Algorithms #SoftwareEngineering

'''


# CODE: SOLUTION

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def validate(self, node: TreeNode | None, low, high) -> bool:
    # Time: O(N)    ||  Space: O(N)
    # Base case: if empty node, valid BST 
        if not node: return True

    # checking node.val exists in range.
        if not low < node.val < high:
            return False
            
    # recursive call for left and right subtree.
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)


    def isValidBST(self, root: TreeNode | None) -> bool:

        return self.validate(root, float("-inf"), float("inf"))
        