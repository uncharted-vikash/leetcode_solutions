'''Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = eceba

Output: 3

The substring is "ece" which has length 3. It contains two distinct characters: 'e' and 'c'.

Example 2:
Input: s = ccaabbb

Output: 5

The substring is "aabbb" which has length 5. It contains two distinct characters: 'a' and 'b'.

Constraints:
1 <= s.length <= 10^5
s consists of English letters.
'''

# code: solutions
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        max_length = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > 2:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
            
