# <-------------------------------Orderly Queue------------------------------->
'''
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string.

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

 

Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
 

Constraints:

1 <= k <= s.length <= 1000
s consist of lowercase English letters.
'''
'''<---------------------------------HARD--------------------------------->'''
# SOLUTION:---

# Intution:
    # _01. k == 1 → You can only rotate the string, so check every rotation and take the lexicographically smallest.
    # _02.  k > 1 → You can rearrange the characters into any order, so simply sort the string.


def orderlyQueue(s: str, k: int) -> str:
    # Time -> O(nlogn) | S.C -> O(N)
    if k > 1:
        return "".join(sorted(s))
        
    # Time -> O(n^2)  | S.C -> O(N)
    result = s
    for i in range(1, len(s)):
        temp = s[i:] + s[:i]
        result = min(result, temp)

    return result

s = "baaca"
k = 3

print(orderlyQueue(s, k))

