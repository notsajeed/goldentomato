# Binary Search

## Intuition

On a **sorted** array, you don't need to check every element — check the middle one. If it's the target, done. If the target is smaller, it must be in the left half (discard the right half entirely); if larger, discard the left half. Each comparison halves the search space, giving O(log n) instead of O(n).

## Definition / How it Works

Maintain `low` and `high` bounds. While `low <= high`:

1. Compute `mid = low + (high - low) / 2` (avoids overflow vs `(low+high)/2`).
2. If `arr[mid] == target`, return `mid`.
3. If `arr[mid] < target`, target is in the right half → `low = mid + 1`.
4. If `arr[mid] > target`, target is in the left half → `high = mid - 1`.
5. If the loop ends without a match, target isn't present.

## Code

```java
int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
```

## Example Problem

**Input:** `arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]`, `target = 23`
**Goal:** find the index of 23.

## Trace

| Step | low | high | mid | arr[mid] | comparison | action   |
| ---- | --- | ---- | --- | -------- | ---------- | -------- |
| 1    | 0   | 9    | 4   | 16       | 16 < 23    | low = 5  |
| 2    | 5   | 9    | 7   | 45       | 45 > 23    | high = 6 |
| 3    | 5   | 6    | 5   | 23       | match!     | return 5 |

**Result:** index `5`, found in 3 comparisons instead of scanning up to 10 elements.

## Complexity

- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive (call stack)

## Key Points / Gotchas

- Array **must** be sorted — sorting an unsorted array first costs O(n log n), which can dominate if you only search once.
- `mid = low + (high - low) / 2` avoids integer overflow that `(low + high) / 2` can cause with large indices — mention this in interviews, it's a common follow-up.
- Variants to know: find first/last occurrence of target (with duplicates), find insertion point (lower_bound/upper_bound), search in rotated sorted array.
- "Binary search on the answer" is a broader pattern: applies to any monotonic predicate, not just array lookup (e.g. minimize/maximize a value satisfying a condition).

## Related

- See also: linear-search, ternary-search
