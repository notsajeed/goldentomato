# Heap Sort

## Intuition

Build a max-heap from the array so the largest element is always at the root. Repeatedly swap the root (max) with the last unsorted element, shrink the heap by one, and re-heapify. Each swap places one more element in its final sorted position at the end of the array. Combines the O(n log n) guarantee of merge sort with the in-place space of quicksort.

## Definition / How it Works

1. **Build max-heap**: convert the array into a binary max-heap (parent ≥ children) — done by calling `heapify` on all non-leaf nodes, bottom-up, O(n) total.
2. **Extract max repeatedly**: swap root (index 0, the max) with the last element of the unsorted region, reduce heap size by 1, then `heapify` the root to restore the heap property. Repeat until heap size is 1.

`heapify(arr, n, i)`: compare node `i` with its children (`2i+1`, `2i+2`); if a child is larger, swap and recursively heapify that subtree.

## Code

```java
void heapSort(int[] arr) {
    int n = arr.length;
    for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        int t = arr[0]; arr[0] = arr[i]; arr[i] = t;
        heapify(arr, i, 0);
    }
}

void heapify(int[] arr, int n, int i) {
    int largest = i, left = 2*i+1, right = 2*i+2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest != i) {
        int t = arr[i]; arr[i] = arr[largest]; arr[largest] = t;
        heapify(arr, n, largest);
    }
}
```

## Example Problem

**Input:** `arr = [4, 10, 3, 5, 1]`
**Goal:** sort in ascending order.

## Trace

**Build max-heap** (start from last non-leaf, index `n/2-1 = 1`):

- `heapify(i=1)`: node 10, children 5,1 → 10 already largest, no change: `[4,10,3,5,1]`
- `heapify(i=0)`: node 4, children 10,3 → 10 larger, swap → `[10,4,3,5,1]`; recurse on index 1 (was 4, now has child 5): 4 vs 5 → swap → `[10,5,3,4,1]`

Heap built: `[10, 5, 3, 4, 1]`

**Extract max repeatedly:**
| Step | Swap root with last | Array | Heapify root over reduced heap | Result |
|---|---|---|---|---|
| 1 | swap arr[0],arr[4] → 10↔1 | [1,5,3,4,**10**] | heapify size 4 | [5,4,3,1,**10**] |
| 2 | swap arr[0],arr[3] → 5↔1 | [1,4,3,**5,10**] | heapify size 3 | [4,1,3,**5,10**] |
| 3 | swap arr[0],arr[2] → 4↔3 | [3,1,**4,5,10**] | heapify size 2 | [3,1,**4,5,10**] |
| 4 | swap arr[0],arr[1] → 3↔1 | [1,**3,4,5,10**] | heap size 1, done | [1,3,4,5,10] |

**Result:** `[1, 3, 4, 5, 10]`

## Complexity

- Time: O(n log n) — all cases (build heap O(n) + n extractions of O(log n) each)
- Space: O(1) — in-place (unlike merge sort)

## Key Points / Gotchas

- Not stable — swaps during heapify can reorder equal elements.
- Slower in practice than quicksort despite same/better big-O, due to poor cache locality (heap operations jump around the array via `2i+1`, `2i+2`).
- Useful when O(n log n) worst-case AND O(1) space are both required — quicksort fails worst-case guarantee, merge sort fails space.
- Directly reusable for "kth largest/smallest element" and priority queue problems — heapify logic is identical.

## Related

- See also: quick, merge
