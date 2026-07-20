# Radix Sort

## Intuition

A non-comparison sort — instead of comparing elements to each other, sort numbers digit by digit, from least significant digit (LSD) to most significant. Each digit-pass uses a stable sort (counting sort) as a subroutine. Because it never compares two full elements directly, it can beat the O(n log n) comparison-sort lower bound, running in O(d·n) where d is the number of digits.

## Definition / How it Works

1. Find the max number to determine the number of digits `d`.
2. For each digit position (starting from least significant — units, then tens, then hundreds...):
   - Run a **stable** counting sort on the array using only that digit as the key.
3. After processing all `d` digit positions, the array is fully sorted.

Stability of the counting sort at each pass is essential — it's what preserves the correct ordering established by earlier (less significant) digit passes.

## Code

```java
void radixSort(int[] arr) {
    int max = Arrays.stream(arr).max().getAsInt();
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSortByDigit(arr, exp);
    }
}

void countingSortByDigit(int[] arr, int exp) {
    int n = arr.length;
    int[] output = new int[n];
    int[] count = new int[10];
    for (int i = 0; i < n; i++) count[(arr[i] / exp) % 10]++;
    for (int i = 1; i < 10; i++) count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % 10;
        output[--count[digit]] = arr[i];
    }
    System.arraycopy(output, 0, arr, 0, n);
}
```

## Example Problem

**Input:** `arr = [170, 45, 75, 90, 802, 24, 2, 66]`
**Goal:** sort in ascending order.

## Trace

Max = 802 → 3 digit positions: units (exp=1), tens (exp=10), hundreds (exp=100).

| Pass         | Digit used        | Array after stable sort on that digit |
| ------------ | ----------------- | ------------------------------------- |
| 1 (units)    | last digit        | [170, 90, 802, 2, 24, 45, 75, 66]     |
| 2 (tens)     | 2nd-to-last digit | [802, 2, 24, 45, 66, 170, 75, 90]     |
| 3 (hundreds) | 3rd-to-last digit | [2, 24, 45, 66, 75, 90, 170, 802]     |

**Result:** `[2, 24, 45, 66, 75, 90, 170, 802]` after 3 digit passes.

## Complexity

- Time: O(d · (n + b)) where d = number of digits, b = base (10 for decimal) — effectively O(n) for fixed-width integers
- Space: O(n + b) — auxiliary output array and count array

## Key Points / Gotchas

- Beats O(n log n) comparison sort lower bound because it isn't a comparison sort — it exploits structure of the keys (fixed-digit numbers).
- Only works cleanly on integers (or fixed-length strings) — not general comparable objects without a digit/character extraction scheme.
- Each digit-pass sort **must** be stable (counting sort qualifies) or the final order breaks.
- For negative numbers, needs a modification (e.g. separate negatives, sort by absolute value, reverse, then combine) — a common "gotcha" question.

## Related

- See also: bucket sort (not in this repo yet), counting sort
