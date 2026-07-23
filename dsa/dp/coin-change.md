# Coin Change

## Intuition

Given a set of coin denominations and a target amount, find the **minimum number of coins** needed to make that amount (assuming unlimited supply of each denomination). Greedy (always pick the largest coin that fits) works for "nice" denomination systems like standard currency, but fails for arbitrary denominations (e.g. coins `[1, 3, 4]` for amount 6 — greedy picks 4+1+1=3 coins, but 3+3=2 coins is better). DP guarantees the correct answer regardless of denomination structure.

## Definition / How it Works

Define `dp[amount]` = minimum coins needed to make exactly `amount`. This is an **unbounded knapsack**-style problem (each coin can be used unlimited times).

Base case: `dp[0] = 0` (zero coins needed to make amount 0).

For each `amount` from 1 to target: `dp[amount] = min(dp[amount - coin] + 1)` over every coin denomination `coin <= amount`. If no valid coin combination exists, leave it as infinity (unreachable).

## Code

```java
int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, Integer.MAX_VALUE);
    dp[0] = 0;

    for (int a = 1; a <= amount; a++) {
        for (int coin : coins) {
            if (coin <= a && dp[a - coin] != Integer.MAX_VALUE) {
                dp[a] = Math.min(dp[a], dp[a - coin] + 1);
            }
        }
    }
    return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
}
```

## Example Problem

**Input:** `coins = [1, 3, 4]`, `amount = 6`
**Goal:** minimum coins to make 6.

## Trace

| amount | Try coin=1: dp[a-1]+1 | Try coin=3: dp[a-3]+1 | Try coin=4: dp[a-4]+1 | dp[amount] = min |
| ------ | --------------------- | --------------------- | --------------------- | ---------------- |
| 0      | — (base case)         | —                     | —                     | 0                |
| 1      | dp[0]+1=1             | — (a<3)               | — (a<4)               | 1                |
| 2      | dp[1]+1=2             | —                     | —                     | 2                |
| 3      | dp[2]+1=3             | dp[0]+1=1             | —                     | 1                |
| 4      | dp[3]+1=2             | dp[1]+1=2             | dp[0]+1=1             | 1                |
| 5      | dp[4]+1=2             | dp[2]+1=3             | dp[1]+1=2             | 2                |
| 6      | dp[5]+1=3             | dp[3]+1=2             | dp[2]+1=3             | **2**            |

**Result:** `dp[6] = 2` — achieved via `3 + 3 = 6` (two coins), correctly beating the greedy answer of 3 coins (4+1+1).

## Complexity

- Time: O(amount × numCoins)
- Space: O(amount)

## Key Points / Gotchas

- **Greedy fails on arbitrary denominations** — this is the classic example to cite when asked "why not just use greedy?" Greedy only works for "canonical" coin systems (like standard currency) where it's provably optimal.
- This is the **unbounded** knapsack pattern (each "item"/coin reusable infinitely) — contrast with 0/1 knapsack where each item is used at most once. The difference shows up in the DP recurrence: no `i` (item index) dimension needed here, since order/count of coin usage doesn't matter, only the running amount.
- Related variant: "coin change II" asks for the **number of distinct ways** to make the amount (not minimum coins) — same table structure, but sums counts instead of taking a min, and needs careful loop ordering (coins outer, amount inner) to avoid counting permutations as distinct combinations.
- Always check for the "impossible" case (`dp[amount]` still infinity) — e.g. `coins = [5]`, `amount = 3` has no solution.

## Related

- See also: knapsack-01, fibonacci-memoization
