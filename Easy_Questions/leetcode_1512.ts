// 🚀 **Day of DSA | LeetCode 1512: Number of Good Pairs**

// 📌 **Intuition**

// Whenever we encounter a number, we need to find how many times the same number has already appeared.

// Each previous occurrence of the current number forms one new good pair with it.

// Instead of checking every possible pair, we can use a Hash Map to keep track of frequencies and count pairs efficiently.

// 💡 **Approach**

// 1. Initialize `count = 0` to store the total number of good pairs.
// 2. Create a Hash Map to store the frequency of each number encountered so far.
// 3. Traverse the array one element at a time:
//    - Get the current number's previous frequency, defaulting to `0`.
//    - Add that frequency to `count`, because each previous occurrence creates one new good pair.
//    - Update the frequency of the current number by incrementing it by one.
// 4. Return `count` as the final answer.

// ⏱️ **Complexity Analysis**

// - **Time Complexity:** O(n) average — we traverse the array once, with average O(1) Hash Map operations.
// - **Auxiliary Space Complexity:** O(k) — where k is the number of distinct elements stored in the Hash Map. In the worst case, O(n).

// 🎯 **Key Takeaway**

// A frequency map can help us count relationships with previously seen elements without checking every possible pair.


function numIdenticalPairss(nums: number[]): number {
    const hashMap: Map<number, number>  = new Map();
    let count: number = 0;

    for (const n of nums) {
        let currentCount: number = hashMap.get(n) ?? 0;

        count += currentCount;

        hashMap.set(n, currentCount + 1);
    }

    return count;
};

