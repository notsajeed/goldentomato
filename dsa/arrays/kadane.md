# Kadane's Algorithm

## Intuition

Find the maximum sum of a contiguous subarray. Brute force checks all O(n²) subarrays. Kadane's observes: at each index, the best subarray ending here is either "extend the previous best" or "start fresh from here" — whichever is larger. This local decision, tracked in a running variable, gives the global answer in one pass.

## Definition / How it Works

Maintain two variables:

- `currentMax` — best subarray sum ending exactly at the current index
- `globalMax` — best subarray sum seen anywhere so far

At each index: `currentMax = max(arr[i], currentMax + arr[i])`. If `currentMax` is greater than `globalMax`, update `globalMax`.

The reset logic (`arr[i]` alone vs `currentMax + arr[i]`) is the core idea — if extending the previous run has become negative/unhelpful, it's better to abandon it and start over at the current element.

## Code

```java
int maxSubArray(int[] arr) {
    int currentMax = arr[0], globalMax = arr[0];
    for (int i = 1; i < arr.length; i++) {
        currentMax = Math.max(arr[i], currentMax + arr[i]);
        globalMax = Math.max(globalMax, currentMax);
    }
    return globalMax;
}
```

## Example Problem

**Input:** `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
**Goal:** find the maximum sum of a contiguous subarray.

## Trace

| i   | arr[i] | currentMax + arr[i] | currentMax = max(arr[i], sum) | globalMax |
| --- | ------ | ------------------- | ----------------------------- | --------- |
| 0   | -2     | —                   | -2                            | -2        |
| 1   | 1      | -2+1=-1             | max(1,-1) = 1                 | 1         |
| 2   | -3     | 1+(-3)=-2           | max(-3,-2) = -2               | 1         |
| 3   | 4      | -2+4=2              | max(4,2) = 4                  | 4         |
| 4   | -1     | 4+(-1)=3            | max(-1,3) = 3                 | 4         |
| 5   | 2      | 3+2=5               | max(2,5) = 5                  | 5         |
| 6   | 1      | 5+1=6               | max(1,6) = 6                  | 6         |
| 7   | -5     | 6+(-5)=1            | max(-5,1) = 1                 | 6         |
| 8   | 4      | 1+4=5               | max(4,5) = 5                  | 6         |

**Result:** `globalMax = 6`, from subarray `[4, -1, 2, 1]` — found in one linear pass instead of checking all 45 possible subarrays.

## Complexity

- Time: O(n)
- Space: O(1)

## Key Points / Gotchas

- If the array can be entirely negative, the answer is the least negative single element — don't default `globalMax` to 0, initialize it to `arr[0]`.
- To also recover the actual subarray (not just sum), track a `start` index that resets whenever `currentMax` resets to `arr[i]`.
- Extension: "maximum circular subarray sum" — compute normal Kadane max, and separately (totalSum − minSubarraySum via inverted Kadane), then take the max of the two (careful with all-negative edge case).
- This is a classic example of dynamic programming with O(1) space — `currentMax` is really `dp[i]`, just not stored as an array.

## Related

- See also: sliding-window, dp (general)
