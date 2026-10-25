'''992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''

# ----------------------------solutions-------------------------------




'''🚀 **LeetCode 992: Subarrays with K Different Integers | Sliding Window**

Today, I solved a challenging subarray problem using the sliding window technique and a frequency hashmap.

### 💡 Intuition

Instead of counting subarrays with exactly `k` distinct integers directly, I used a mathematical trick:

**Exactly K = At Most K − At Most (K − 1)**

This transforms the problem into two simpler sliding window problems.

### ⚙️ Approach

1. Use a sliding window and a frequency hashmap to track distinct integers.
2. If the window contains more than `k` distinct integers, shrink it from the left until it becomes valid.
3. For every valid window, add `right - left + 1` to count all valid subarrays ending at the current `right` index.
4. Calculate the final answer by subtracting:

   `atMost(k) - atMost(k - 1)`

### ⏱️ Complexity Analysis

- **Time Complexity:** O(n) — Each pointer traverses the array at most once per sliding window calculation.
- **Auxiliary Space Complexity:** O(k) — The frequency hashmap stores at most `k` distinct integers in the first calculation.

### 🎯 Key Takeaway

Sometimes, solving a problem indirectly makes it much easier. The transformation from *exactly K* to *at most K minus at most K − 1* is a powerful technique for subarray problems.
'''



# CODE: SOLUTIONS

class Solution:
    def sliding_window(self, arr: list[int], k: int) -> int:
        count = 0
        left = 0
        freq = {}

        for right in range(len(arr)):
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            while len(freq) > k:
                freq[arr[left]] -= 1

                if freq[arr[left]] == 0:
                    del freq[arr[left]]

                left += 1

            count += right - left + 1
        
        return count

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.sliding_window(nums, k) - self.sliding_window(nums, k-1)

        