# Linear Search

## Intuition

The simplest possible search: check every element one by one until you find the target or run out of elements. No assumptions about the data (unsorted is fine) — the tradeoff is it can't do better than O(n).

## Definition / How it Works

Start at index 0, compare each element to the target. If it matches, return the index. If the loop finishes without a match, the target isn't present.

## Code

```java
int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```

## Example Problem

**Input:** `arr = [4, 2, 9, 7, 5]`, `target = 7`
**Goal:** find the index of 7.

## Trace

| i   | arr[i] | match?         |
| --- | ------ | -------------- |
| 0   | 4      | no             |
| 1   | 2      | no             |
| 2   | 9      | no             |
| 3   | 7      | yes → return 3 |

**Result:** index `3`, found after checking 4 elements.

## Complexity

- Time: O(n) worst/average case, O(1) best case (target at index 0)
- Space: O(1)

## Key Points / Gotchas

- Only algorithm that works on unsorted data without preprocessing — binary search requires sorted input.
- Rarely the "intended" answer in interviews unless the array is explicitly unsorted or small; mentioning it as a baseline before jumping to a better approach shows good reasoning.
- No sorted-order requirement makes it the fallback for linked lists too, where random access (needed for binary search) isn't available.

## Related

- See also: binary-search
