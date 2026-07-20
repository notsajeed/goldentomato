# Merge Sort

## Intuition

A divide-and-conquer sort: split the array in half recursively until pieces are size 1 (trivially sorted), then merge pairs of sorted pieces back together in order. Merging two sorted arrays is O(n), and there are O(log n) levels of splitting, giving O(n log n) overall — much better than O(n²) comparison sorts.

## Definition / How it Works

1. **Divide**: split array into two halves at the midpoint, recursively sort each half.
2. **Conquer (merge)**: given two sorted halves, walk through both with pointers, always picking the smaller front element into a new output array, until both halves are exhausted.
3. Base case: a subarray of size 0 or 1 is already sorted.

## Code

```java
void mergeSort(int[] arr, int left, int right) {
    if (left >= right) return;
    int mid = (left + right) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

void merge(int[] arr, int left, int mid, int right) {
    int[] temp = new int[right - left + 1];
    int i = left, j = mid + 1, k = 0;
    while (i <= mid && j <= right) {
        temp[k++] = (arr[i] <= arr[j]) ? arr[i++] : arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    System.arraycopy(temp, 0, arr, left, temp.length);
}
```

## Example Problem

**Input:** `arr = [38, 27, 43, 3]`
**Goal:** sort in ascending order.

## Trace

**Divide phase:**

```
[38, 27, 43, 3]
   /          \
[38, 27]    [43, 3]
  /   \       /   \
[38]  [27]  [43]  [3]
```

**Merge phase (bottom-up):**
| Merge step | Inputs | Compare | Output |
|---|---|---|---|
| 1 | [38] + [27] | 38 vs 27 → 27 first | [27, 38] |
| 2 | [43] + [3] | 43 vs 3 → 3 first | [3, 43] |
| 3 | [27,38] + [3,43] | 27 vs 3→3, 27 vs 43→27, 38 vs 43→38, remaining 43 | [3, 27, 38, 43] |

**Result:** `[3, 27, 38, 43]`

## Complexity

- Time: O(n log n) — all cases (best, average, worst)
- Space: O(n) — needs auxiliary array for merging (not in-place)

## Key Points / Gotchas

- Stable sort — critical for multi-key sorting (e.g. sort by date, then by name, preserving date order among same-name entries).
- The O(n) extra space is the main tradeoff vs quicksort's O(log n) — matters for memory-constrained environments/embedded systems.
- Guaranteed O(n log n) even in worst case, unlike quicksort's O(n²) worst case — preferred when worst-case guarantees matter (e.g. real-time systems).
- Used as the backbone of external sorting (sorting data too large for memory) because it processes data in sequential chunks.

## Related

- See also: quick, kadane
