# 🌳 **LeetCode 958 — Check Completeness of a Binary Tree**

'''
Another binary tree problem done! 🚀

Today I practiced **LeetCode 958: Check Completeness of a Binary Tree**.

The key idea was actually very simple:

👉 **Once we encounter a `None` during BFS, we should not find any real node after it.**

I used **BFS (Breadth-First Search)** with a queue to traverse the tree level by level.

### 🧠 My Approach

* Use a queue for BFS.
* Keep track of whether we have already seen a `None`.
* If `None` is found, set `seen_null = True`.
* If a real node appears after that, the tree is **not complete**.
* Otherwise, the tree is complete.

### 💡 What I learned

The most important part wasn't just solving the problem, but understanding **why** the `seen_null` condition works.

> **"Pehle None mil gaya → uske baad sirf None milna chahiye."**

This simple thought helped me understand the problem much better. 😄

⏱️ **Time Complexity:** O(n)
💾 **Space Complexity:** O(n)

Continuing my journey of learning Data Structures & Algorithms, one problem at a time. 💪

#LeetCode #DSA #BinaryTree #BFS #Python #CodingJourney #ProblemSolving #100DaysOfCode #LearningInPublic

    
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
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        q = deque([root])
    
    # to see, in past None node contains or not
        seen_null = False

        while q:
            node = q.popleft()

        # agar node None hai, means ak empty position mil gyi.
            if not node:
                seen_null = True

            else:
            # Agar pehle hi None mil chuka hai. 
            # aur ab real node mil rahi hai, tree complete nahi hai.
                if seen_null:
                    return False

            # left and right child ko queue mein daal do.
            # child None bhi ho sakta hai.
                q.append(node.left) 
                q.append(node.right) 

    # agar None ke baad koi real node nhi mili.
    # to tree complete hai.
        return True 
    

            

        