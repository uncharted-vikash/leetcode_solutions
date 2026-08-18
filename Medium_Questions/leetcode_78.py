# **LeetCode 78 — Subsets | Backtracking Intuition & Complexity**

'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''






'''
Intuition
The key idea is: for every element, we have exactly 2 choices:
Include nums[index] in the current subset.
Skip nums[index].
Complexity
Time complexity:
<There are 2^n possible subsets.
For every subset, we copy the path into result, which can take up to O(n).

Overall: O(n × 2^n)

Space complexity:
Space: O(n × 2^n)
'''

# CODE SOLUTION(Medium):---------

def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(index, path):
        # Base Case
        if index == len(nums):
            result.append(path[:])
            return

        # Decision_01: include it nums[index]
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

        # Dicision_02: skip nums[index]
        backtrack(index + 1, path)

    backtrack(0, [])

    return result

nums = [1,2,3]

print(subsets(nums))

