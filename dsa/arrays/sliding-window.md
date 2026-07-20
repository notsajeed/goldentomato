# Sliding Window

## Intuition

When a problem asks for something about every contiguous subarray/substring (max sum, longest substring with a property, smallest window containing X), recomputing from scratch for each window is wasteful. Instead, maintain a window with two pointers and update it incrementally as it slides.

## Definition / How it Works

Two variants:

- **Fixed size window**: window size `k` is given. Slide by adding the new right element and removing the leftmost element every step. O(n) total instead of O(n·k).
- **Variable size window**: expand `right` to grow the window; shrink from `left` when a constraint is violated (e.g. sum exceeds target, duplicate found, more than K distinct chars). The window only ever expands or shrinks — never resets — which is what keeps it O(n).

General template for variable window:

```
left = 0
for right in range(n):
    add arr[right] to window state
    while window violates constraint:
        remove arr[left] from window state
        left++
    update answer using current window [left, right]
```

## Code

```java
// Longest substring without repeating characters
int lengthOfLongestSubstring(String s) {
    Set<Character> window = new HashSet<>();
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); right++) {
        while (window.contains(s.charAt(right))) {
            window.remove(s.charAt(left));
            left++;
        }
        window.add(s.charAt(right));
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

## Example Problem

**Input:** `s = "abcabcbb"`
**Goal:** find the length of the longest substring without repeating characters.

## Trace

| right | char | window before | duplicate? | shrink (left moves)       | window after | maxLen |
| ----- | ---- | ------------- | ---------- | ------------------------- | ------------ | ------ |
| 0     | a    | {}            | no         | —                         | {a}          | 1      |
| 1     | b    | {a}           | no         | —                         | {a,b}        | 2      |
| 2     | c    | {a,b}         | no         | —                         | {a,b,c}      | 3      |
| 3     | a    | {a,b,c}       | yes        | remove a (left→1)         | {b,c,a}      | 3      |
| 4     | b    | {b,c,a}       | yes        | remove b (left→2)         | {c,a,b}      | 3      |
| 5     | c    | {c,a,b}       | yes        | remove c (left→3)         | {a,b,c}      | 3      |
| 6     | b    | {a,b,c}       | yes        | remove a, then b (left→5) | {c,b}        | 3      |
| 7     | b    | {c,b}         | yes        | remove c, then b (left→7) | {b}          | 3      |

**Result:** `maxLen = 3` (e.g. "abc") — computed in one pass instead of checking all O(n²) substrings.

## Complexity

- Time: O(n) — each element is added and removed from the window at most once
- Space: O(k) where k is window/character-set size (O(1) if bounded alphabet)

## Key Points / Gotchas

- The "each pointer moves forward only" property is what gives O(n), not O(n²) — don't reset `left` to 0 inside the loop.
- For fixed-size windows, watch the boundary: window is valid only once `right >= k - 1`.
- Common tell in problem statement: "contiguous subarray/substring", "at most K", "longest/shortest window satisfying...".
- Distinguish from two-pointer: sliding window always maintains a _contiguous_ range with running aggregate state (sum, count map, set).

## Related

- See also: two-pointer, kadane
