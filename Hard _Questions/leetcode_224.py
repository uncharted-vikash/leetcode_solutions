# Leetcode_224: Basic Calculator —> Stack + Sign Tracking | O(n) Time, O(n) Space


'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''




'''
Intuition
The expression contains numbers, +, -, and parentheses.
1. Build multi-digit numbers using number = number * 10 + digit.
2. sign stores whether the current number should be added (+1) or subtracted (-1).
3. When we see + or -, add the previous number to result.
4. When we see (, save the current result and sign in the stack, then start calculating the expression inside the parentheses.
5. When we see ), finish the current expression, then restore the previous sign and result from the stack.
6. Finally, add the last number to result.

Key idea: The stack remembers the calculation state before entering each parenthesis.

Complexity
Time: O(n) — each character is processed once.
Space: O(n) — in the worst case, nested parentheses can make the stack size O(n).

'''

# <--------------------------CODE SOLUTION:-------------------------->

def calculate(s: str) -> int:
    stack = []
    number, sign, result = 0, 1, 0

    for ch in s:
        if ch.isdigit():
            # Create number
            number = (number*10) + ord(ch) - ord('0')
        elif ch == '+':
            # Add number in result
            result += (number*sign)
            number = 0
            sign = 1
        
        elif ch == '-':
            # Add number in result
            result += (number*sign)
            number = 0
            sign = -1

        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            number = 0
            sign = 1

        elif ch == ')':
            result += (number*sign)
            number = 0

            stack_sign = stack.pop()
            last_value = stack.pop()

            result *= stack_sign
            result += last_value

            
    # for this type problem -> "1+1"
    result += (number*sign)

    return result

print(calculate(s = "(1+(4+5+2)-3)+(6+8)"))


