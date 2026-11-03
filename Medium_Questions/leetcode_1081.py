'''
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 
Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.'''


# CODE: SOLUTIONS
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
    