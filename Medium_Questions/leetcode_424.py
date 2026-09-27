# 🚀 **LeetCode 424 — Longest Repeating Character Replacement**

'''

### 🔥 Turning a Sliding Window Into a Powerful Pattern

**💡 Intuition**
Keep a window where we can make all characters the same using at most `k` replacements.
The key idea: **Window Size − Most Frequent Character Count = Characters We Need to Replace.**

**⚡ Approach**

* Expand the window using the right pointer.
* Track character frequencies.
* If replacements needed > `k`, shrink from the left.
* Keep updating the maximum valid window length.

**⏱️ Complexity**

* **Time:** O(N)
* **Space:** O(K) — at most the number of distinct characters tracked.

🧠 **Key Takeaway:**
Sometimes the trick isn't changing the entire window—it's identifying the **most frequent character** and calculating how many changes are actually needed.

#LeetCode #DSA #Python #SlidingWindow #CodingInterview #ProblemSolving #100DaysOfCode

'''

#   <------------------------------------------------------------------->

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''


# CODE: SOLUTIONS

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        my_dict = {}
        left = 0

        for right in range(len(s)):
        # count the frequency of each character in the window.
            my_dict[s[right]] = my_dict.get(s[right], 0) + 1

        # If the number of characters we need to replace is greater than k,
        # shrink the window from the left.
            while (right - left + 1) - max(my_dict.values()) > k:
                my_dict[s[left]] -= 1
                left += 1

        # update the maximum valid window length.
            max_length = max(max_length, right - left + 1)

        return max_length

        