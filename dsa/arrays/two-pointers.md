# Two Pointer

## Intuition

Instead of checking every pair of elements with nested loops (O(n²)), use two indices that move through the array based on a condition, cutting work down to O(n). Works when the array is sorted or has some monotonic property you can exploit.

## Definition / How it Works

Two pointers usually start at opposite ends (converging) or both at the start (fast/slow). At each step, compare the values at the pointers and move one or both based on a rule:

- **Converging pair** (e.g. pair sum in sorted array): start `left = 0`, `right = n-1`. If sum too small, move `left++`. If too large, move `right--`.
- **Fast/slow pair** (e.g. cycle detection, removing duplicates): both start at index 0, one moves faster or only one moves when a condition holds.

The key invariant: every move must provably discard elements that can no longer be part of the answer.

## Code

```java
// Two Sum on sorted array
int[] twoSum(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return new int[]{left, right};
        else if (sum < target) left++;
        else right--;
    }
    return new int[]{-1, -1};
}
```

## Example Problem

**Input:** `arr = [2, 7, 11, 15, 20]`, `target = 26`
**Goal:** find indices of two numbers that add up to 26.

## Trace

| Step | left | right | arr[left] | arr[right] | sum | action                      |
| ---- | ---- | ----- | --------- | ---------- | --- | --------------------------- |
| 1    | 0    | 4     | 2         | 20         | 22  | 22 < 26 → left++            |
| 2    | 1    | 4     | 7         | 20         | 27  | 27 > 26 → right--           |
| 3    | 1    | 3     | 7         | 15         | 22  | 22 < 26 → left++            |
| 4    | 2    | 3     | 11        | 15         | 26  | match found → return [2, 3] |

**Result:** `[2, 3]` (values 11 + 15 = 26) found in 4 steps instead of checking all 10 pairs.

## Complexity

- Time: O(n)
- Space: O(1)

## Key Points / Gotchas

- Requires sorted input for the converging variant — sort first if unsorted (adds O(n log n)).
- Don't confuse with sliding window — two pointer doesn't necessarily maintain a contiguous "window" of fixed meaning, it's about narrowing a search space.
- Classic use cases: pair sum, container with most water, trapping rain water, merging two sorted arrays, removing duplicates in-place.
- Off-by-one errors on `left < right` vs `left <= right` are the most common bug — think through the boundary case by hand.

## Related

- See also: sliding-window, merge (sort)
