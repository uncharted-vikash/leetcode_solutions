# Leetcode_239: Sliding Window Maximum
'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

# SOLUTION: 
'''
Approach
“I’ll use a monotonic decreasing deque to maintain the maximum of the current window.”

1. Store indices in the deque, not values.
2. Remove indices from the front if they are outside the current window.
3. Before adding the current index, remove from the back all indices whose values are smaller than nums[i].
4. The front of the deque is always the maximum of the current window.
5. When the window reaches size k, add nums[deque[0]] to the answer.
    Complexity
    complexity:
    Time: O(n)
    Space: O(k)
'''
from collections import deque
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    q = deque()
    ans = []
    left = 0
    for right in range(len(nums)):
        # pop smaller value form q
        while q and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)
        # remove left value from window
        if left > q[0]:
            q.popleft()

        if (right + 1) >= k:
            ans.append(nums[q[0]]) 
            left += 1

    return ans

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums, k))

