'''Leetcode_1662: Check If Two String Arrays are Equivalent'''

'''Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.



Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.'''

# <---------------------Easy--------------------->


def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
# <---------------------Aproach _01: T.C -> O(N) and S.C -> O(N)--------------------->

    s1 = "".join(word1)
    s2 = "".join(word2)

    return s1 == s2

# <---------------- Aproach_02: T.C -> O(N) and S.C -> O(1) (two pointer) ---------------->

    i, j = 0, 0
    p, q = 0, 0
    # p :- strings of word1
    # i :- character of string p
    # q :- strings of word2
    # j :- character of string q

    while p < len(word1) and q < len(word2):
        if word1[p][i] != word2[q][j]: 
            return False

        i += 1
        j += 1

        if i == len(word1[p]):
            p += 1
            i = 0

        if j == len(word2[q]):
            q += 1
            j = 0

    return p == len(word1) and q == len(word2)

print(arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
            
















