/**🚀 Day X of #100DaysOfCode / #DSA Challenge!
Today I tackled LeetCode 796: Rotate String 🔄

🧩 The Problem

Given two strings s and goal, return true if s can become goal after a certain number of shifts (moving the leftmost character to the right end).

💡 The Clever Approach (The Substring Trick)

Instead of manually simulating the shifts step-by-step (which is inefficient), we can use a highly elegant mathematical property of strings:
1. Length Check: If s and goal have different lengths, it's immediately impossible. Return false.
2. Concatenation: Concatenate s with itself (s + s).
3. The Trick: The string s + s contains all possible rotations of s as substrings. Therefore, if goal is a valid rotation, it must exist inside s + s.

📊 Complexity

• Time Complexity: O(N) or O(N²) depending on the underlying substring search algorithm (contains / indexOf).
• Space Complexity: O(N) to store the concatenated string.

🧠 Key Takeaway

Sometimes a problem that looks like it requires a complex loop or simulation can be reduced to a single, clever string operation. Always look for structural patterns before writing tedious logic!
#LeetCode #CodingJourney #SoftwareEngineering #DataStructures #Algorithms
Try without personalization
*/



// CODE: SOLUTIONS

/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    if (s.length != goal.length) {
        return false;
    }

    let concatenation = s + s;

    if (concatenation.includes(goal)){
        return true;
    }

    return false;
};
