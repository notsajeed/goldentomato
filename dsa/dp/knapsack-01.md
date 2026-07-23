# 0/1 Knapsack

## Intuition

Given items each with a weight and value, and a knapsack with a fixed weight capacity, pick a subset of items maximizing total value without exceeding capacity — each item can be taken entirely or not at all (hence "0/1", as opposed to fractional knapsack where partial items are allowed). Brute force tries all 2ⁿ subsets; DP instead builds up the answer using the fact that "best value using the first i items with capacity w" only depends on smaller subproblems.

## Definition / How it Works

Define `dp[i][w]` = maximum value achievable using the first `i` items with capacity `w`.

For each item `i` (weight `wt[i]`, value `val[i]`), two choices:

- **Skip item i**: `dp[i][w] = dp[i-1][w]`
- **Take item i** (only possible if `wt[i] <= w`): `dp[i][w] = val[i] + dp[i-1][w - wt[i]]`

Take the max of the two options: `dp[i][w] = max(skip, take)`.

Base case: `dp[0][w] = 0` for all w (no items → no value).

## Code

```java
int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            int skip = dp[i - 1][w];
            int take = (weights[i - 1] <= w)
                ? values[i - 1] + dp[i - 1][w - weights[i - 1]]
                : 0;
            dp[i][w] = Math.max(skip, take);
        }
    }
    return dp[n][capacity];
}
```

## Example Problem

**Input:** items `[(weight=1,value=6), (weight=2,value=10), (weight=3,value=12)]`, capacity = 5
**Goal:** maximum value achievable.

## Trace

`dp[i][w]` table (rows = items considered so far, cols = capacity 0..5):

| i \ w         | 0   | 1   | 2   | 3   | 4   | 5   |
| ------------- | --- | --- | --- | --- | --- | --- |
| 0 (no items)  | 0   | 0   | 0   | 0   | 0   | 0   |
| 1 (wt1,val6)  | 0   | 6   | 6   | 6   | 6   | 6   |
| 2 (wt2,val10) | 0   | 6   | 10  | 16  | 16  | 16  |
| 3 (wt3,val12) | 0   | 6   | 10  | 16  | 18  | 22  |

**Key cell walkthrough — dp[3][5]:** skip item 3 → `dp[2][5] = 16`. Take item 3 (wt=3 ≤ 5) → `12 + dp[2][5-3] = 12 + dp[2][2] = 12 + 10 = 22`. `max(16, 22) = 22`.

**Result:** `dp[3][5] = 22` — achieved by taking item 2 (wt2,val10) + item 3 (wt3,val12) = weight 5, value 22.

## Complexity

- Time: O(n × capacity)
- Space: O(n × capacity), reducible to O(capacity) using a 1D rolling array (iterate `w` in **descending** order to avoid using an item twice)

## Key Points / Gotchas

- The 1D space optimization requires iterating `w` from high to low within each item's pass — iterating ascending would let the same item be "reused" (that's actually how the _unbounded_ knapsack variant works, where infinite copies of each item are allowed).
- 0/1 knapsack is NP-complete in general (pseudo-polynomial time here — O(n × capacity) is polynomial in the _value_ of capacity, not its _bit-length_, so it's slow for very large capacities).
- Recognize this pattern in disguise: "subset sum" (can we hit an exact target sum?) is knapsack with value = weight; "partition equal subset sum," "target sum" are all knapsack variants.
- To recover _which_ items were chosen (not just the max value), backtrack through the table from `dp[n][capacity]`: if `dp[i][w] != dp[i-1][w]`, item i was taken.

## Related

- See also: fibonacci-memoization, coin-change
