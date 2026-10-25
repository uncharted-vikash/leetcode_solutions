'''1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length'''


#-----------------------solution----------------------------

'''🚀 **LeetCode 1248: Count Number of Nice Subarrays | Sliding Window**

Today, I solved the problem of counting the number of subarrays containing exactly `k` odd numbers.

### 💡 Intuition
A subarray is called *nice* if it contains exactly `k` odd numbers.

Instead of generating every possible subarray, I used a sliding window with three pointers: `left`, `mid`, and `right`.

The key insight is that multiple valid subarrays can end at the same `right` index. By tracking the position of the first odd number using `mid`, we can count these subarrays efficiently.

### ⚙️ Approach
1. Expand the window by moving `right` and count the odd numbers.
2. If the window contains more than `k` odd numbers, move `left` forward until the window becomes valid, then reset `mid` to `left`.
3. When the window contains exactly `k` odd numbers, move `mid` past the leading even numbers to locate the first odd number.
4. Count all valid starting positions using:

   `res += (mid - left) + 1`

5. Repeat until all elements have been processed.

### ⏱️ Complexity Analysis
- **Time Complexity:** O(n) — Each pointer moves only forward through the array.
- **Auxiliary Space Complexity:** O(1) — Only a constant number of variables are used.

### 🎯 Key Takeaway
The most interesting part of this problem was understanding how the `mid` pointer helps count multiple valid subarrays ending at the same index without checking each subarray individually.'''


# CODE: SOLUTIONS
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd, res = 0, 0
        left, mid = 0, 0

        for right in range(len(nums)):
            if nums[right] % 2:
                odd += 1
        

            while odd > k:
                if nums[left] % 2:
                    odd -= 1
                
                left += 1
                mid = left

        
            if odd == k:
                while nums[mid] % 2 == 0:
                    mid += 1
            # The distance from 'left' to 'mid' represents all the valid subarray
                res += (mid - left) + 1

        return res

    