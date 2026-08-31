# Judge Square Sum — Two Pointer Approach
'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
'''



'''
# Intuition
We need to find two integers a and b such that:

a² + b² = c

Instead of checking every possible pair, use two pointers.

*  left = 0 → smallest possible number.
*  right = √c → largest possible number, because no number greater than √c can have its square ≤ c.
*  Calculate left² + right².
    * If it equals c → found the answer.
    * If it is greater than c → decrease right.
    * If it is smaller than c → increase left.

This works because increasing left increases the sum, while decreasing right decreases the sum.

# Approach
* Set left = 0.
* Set right = floor(√c).
* While left <= right:
    * Calculate left² + right².
    * If equal to c, return True.
    * If greater than c, move right left.
    * Otherwise, move left right.
* If no pair is found, return False.

# Complexity
- Time complexity:
Time: O(√c)

- Space complexity:
Space: O(1)
'''

def judgeSquareSum(c: int) -> bool:
    left = 0 # left pointer starts at 0
    right = int(c**0.5) # right pointer starts at the integer square root of c
    
    while left <= right:
        # Calculate sum of squares of the two pointers
        curr_sum = left*left + right*right
        if curr_sum == c:
            return True # if sum equals to c, return True

        elif curr_sum > c:
            right -= 1  # if sum greater then c, move right pointer left

        else: # curr_sum < c
            left += 1 # if sum less then c, move left pointer right

    return False # if no such pair is found, return False 

print(judgeSquareSum(c = 25))


