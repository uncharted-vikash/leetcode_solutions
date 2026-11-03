'''Given a string s, remove duplicate letters so that every letter appears once and only once. The relative order of the letters that were not removed must be preserved. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''
# <------------------------------------------------------------------------>

'''
# Remove Duplicate Letters | Greedy + Monotonic Stack

### 💡 Intuition
The goal is to remove duplicate characters while keeping the lexicographically smallest possible subsequence containing every distinct character exactly once.

The key observation is:

If the current character is smaller than the character at the top of the stack, we should consider removing the stack's top character to get a lexicographically smaller result.

However, we can only remove it if it appears again later in the string. Otherwise, we would lose that character completely.

### ⚙️ Approach

1. **Store Last Occurrences:** Traverse the string and store the last index of every character in a dictionary. This helps determine whether a character can safely be removed.

2. **Use a Stack and Set:** Maintain a stack to build the lexicographically smallest subsequence and a set to keep track of characters already included.

3. **Skip Duplicates:** If the current character is already present in the set, skip it.

4. **Maintain Lexicographical Order:** While the stack is not empty, check:
   - The top character is greater than the current character.
   - The top character appears again later in the string.

   If both conditions hold, pop it from the stack and remove it from the set.

5. **Push Current Character:** Add the current character to the stack and mark it as seen.

6. **Build the Result:** Join the stack to get the final answer.

### ⏱️ Complexity Analysis

- **Time Complexity: O(n)** — We traverse the string twice. Each character is pushed and popped from the stack at most once.
- **Space Complexity: O(1)** — Assuming lowercase English letters, the dictionary, set, and stack store at most 26 distinct characters.

### 📌 Key Takeaway
This problem demonstrates how Greedy + Monotonic Stack can help construct the lexicographically smallest subsequence while ensuring every distinct character appears exactly once.

'''

# CODE: SOLUTION

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}

        for i, ch in enumerate(s):
            last_index[ch] = i

        seen = set()
        stack = []

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and stack[-1] > ch and last_index[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)
    