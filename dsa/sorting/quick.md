# Quick Sort

## Intuition

Also divide-and-conquer, but instead of splitting evenly and merging afterward, quicksort picks a "pivot" element and partitions the array so everything smaller is to its left and everything larger is to its right. The pivot is now in its final sorted position. Recurse on the two partitions. No merge step needed — partitioning does the work in place.

## Definition / How it Works

1. Choose a pivot (commonly last element, first element, or random — random avoids worst-case on sorted input).
2. **Partition**: rearrange the array so elements `< pivot` come before it and elements `>= pivot` come after. Return pivot's final index.
3. Recursively quicksort the left partition and right partition.

Lomuto partition scheme (simplest to code):

```
partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j = low to high-1:
        if arr[j] < pivot:
            i++; swap(arr[i], arr[j])
    swap(arr[i+1], arr[high])
    return i + 1
```

## Code

```java
void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int t = arr[i]; arr[i] = arr[j]; arr[j] = t;
        }
    }
    int t = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = t;
    return i + 1;
}
```

## Example Problem

**Input:** `arr = [10, 7, 8, 9, 1, 5]`
**Goal:** sort in ascending order. Pivot = last element each call.

## Trace

**First partition call** — `low=0, high=5`, pivot = `arr[5] = 5`, `i = -1`
| j | arr[j] | arr[j] < 5? | action | i |
|---|---|---|---|---|
| 0 | 10 | no | — | -1 |
| 1 | 7 | no | — | -1 |
| 2 | 8 | no | — | -1 |
| 3 | 9 | no | — | -1 |
| 4 | 1 | yes | i++ , swap(arr[0],arr[4]) → [1,7,8,9,10,5] | 0 |

Final swap: `arr[i+1]=arr[1]` with `arr[high]=arr[5]` → `[1, 5, 8, 9, 10, 7]`. Pivot 5 now at index 1 (correct final position).

**Recurse left** on `[1]` (already sorted, size 1). **Recurse right** on `[8, 9, 10, 7]` (indices 2–5) — repeats the same partition process until fully sorted.

**Result:** `[1, 5, 7, 8, 9, 10]`

## Complexity

- Time: O(n log n) average, O(n²) worst case (already-sorted array with bad pivot choice, e.g. always picking last element)
- Space: O(log n) — recursion stack (in-place partitioning, no extra array)

## Key Points / Gotchas

- Worst case O(n²) happens when the pivot is always the min or max (e.g. sorted array + last-element pivot) — random pivot or median-of-three mitigates this.
- Not stable by default (Lomuto/Hoare partition can reorder equal elements).
- In practice often faster than merge sort due to better cache locality (in-place, smaller constant factor) despite same average complexity.
- Interview follow-up to expect: "what if array has many duplicate values?" → use 3-way partitioning (Dutch national flag) to group `< pivot`, `== pivot`, `> pivot`.

## Related

- See also: merge, heap
