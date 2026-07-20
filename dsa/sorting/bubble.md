# Bubble Sort

## Intuition

Repeatedly step through the array, compare adjacent elements, and swap them if they're in the wrong order. Larger elements "bubble up" to the end with each pass. Simple to reason about, but inefficient — mainly useful as a teaching baseline, not for real use.

## Definition / How it Works

For each pass through the array, compare every adjacent pair. If `arr[j] > arr[j+1]`, swap them. After one full pass, the largest unsorted element is guaranteed to be at its correct final position. Repeat for `n-1` passes. Add an early-exit flag: if a pass makes zero swaps, the array is already sorted — stop early.

## Code

```java
void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        boolean swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted
    }
}
```

## Example Problem

**Input:** `arr = [5, 1, 4, 2, 8]`
**Goal:** sort in ascending order.

## Trace

| Pass | Array state during pass                              | Swaps made | Array after pass                       |
| ---- | ---------------------------------------------------- | ---------- | -------------------------------------- |
| 1    | compare (5,1)→swap, (5,4)→swap, (5,2)→swap, (5,8)→no | 3          | [1, 4, 2, 5, 8]                        |
| 2    | compare (1,4)→no, (4,2)→swap, (4,5)→no               | 1          | [1, 2, 4, 5, 8]                        |
| 3    | compare (1,2)→no, (2,4)→no                           | 0          | [1, 2, 4, 5, 8] — no swaps, exit early |

**Result:** `[1, 2, 4, 5, 8]` in 3 passes instead of the full 4 (n-1), thanks to early exit.

## Complexity

- Time: O(n²) worst/average, O(n) best case (already sorted, with early-exit flag)
- Space: O(1) — in-place

## Key Points / Gotchas

- Always mention the early-exit optimization in interviews — it's the difference between "naive" and "acceptable" bubble sort.
- Stable sort (equal elements retain relative order) — matters when sorting objects by one key but need to preserve another.
- Never use in production for large n; it's asked mainly to test understanding of comparison-based sorting basics.
- Contrast with selection sort: bubble sort swaps adjacent pairs repeatedly, selection sort finds the min and places it directly — selection sort does fewer swaps but same O(n²) comparisons.

## Related

- See also: merge, quick
