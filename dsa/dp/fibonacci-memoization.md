# Fibonacci — Memoization & Tabulation

## Intuition

The naive recursive Fibonacci (`fib(n) = fib(n-1) + fib(n-2)`) recomputes the same subproblems exponentially many times — `fib(5)` calls `fib(3)` twice, `fib(2)` three times, and so on. Dynamic programming's core idea: **cache the result of each subproblem the first time it's computed**, so it's never recomputed. This turns exponential O(2ⁿ) into linear O(n). Fibonacci is the canonical example for learning the two DP styles: top-down memoization and bottom-up tabulation.

## Definition / How it Works

**Top-down (memoization)**: keep the natural recursive structure, but store each result in a cache (array or map) the first time it's computed. Before recursing, check the cache — if present, return immediately instead of recomputing.

**Bottom-up (tabulation)**: flip the direction — start from the base cases and iteratively build up to `fib(n)`, storing each result in an array (or just two rolling variables, since Fibonacci only needs the last two values).

## Code

```java
// Top-down memoization
Map<Integer, Long> memo = new HashMap<>();
long fibMemo(int n) {
    if (n <= 1) return n;
    if (memo.containsKey(n)) return memo.get(n);
    long result = fibMemo(n - 1) + fibMemo(n - 2);
    memo.put(n, result);
    return result;
}

// Bottom-up tabulation, O(1) space
long fibTab(int n) {
    if (n <= 1) return n;
    long prev2 = 0, prev1 = 1;
    for (int i = 2; i <= n; i++) {
        long curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

## Example Problem

**Input:** `n = 5`
**Goal:** compute `fib(5)`.

## Trace

**Naive recursion call tree for fib(5)** (no memoization) — note `fib(3)` computed twice, `fib(2)` three times:

```
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)     ← fib(3) computed again here
fib(3) = fib(2) + fib(1)     ← fib(2) computed again here
```

**With memoization**, each `fib(k)` computed exactly once:
| Call | Cache hit? | Computed value | Cache after |
|---|---|---|---|
| fibMemo(5) | no | needs fib(4)+fib(3) | — |
| fibMemo(4) | no | needs fib(3)+fib(2) | — |
| fibMemo(3) | no | needs fib(2)+fib(1) | — |
| fibMemo(2) | no | fib(1)+fib(0) = 1+0 = 1 | {2:1} |
| fibMemo(1) | base case | returns 1 | — |
| fibMemo(3) resolves | — | fib(2)+fib(1) = 1+1 = 2 | {2:1, 3:2} |
| fibMemo(2) again (from fib(4)) | **yes, cache hit** | returns 1 instantly | — |
| fibMemo(4) resolves | — | fib(3)+fib(2) = 2+1 = 3 | {2:1,3:2,4:3} |
| fibMemo(5) resolves | — | fib(4)+fib(3) = 3+2 = 5 | {...,5:5} |

**Result:** `fib(5) = 5`, computed with only 5 unique subproblem calculations instead of the naive version's 15 total calls (many redundant).

## Complexity

- Naive recursion: O(2ⁿ) time, O(n) space (call stack)
- Memoization: O(n) time, O(n) space (cache + call stack)
- Tabulation (rolling variables): O(n) time, O(1) space

## Key Points / Gotchas

- Tabulation with just two rolling variables (`prev1`, `prev2`) instead of a full array is the space-optimized version — recognize when a DP only needs the last k states, not the entire history.
- Memoization is often easier to derive from the naive recursive solution (add a cache check + cache write), while tabulation requires figuring out the correct iteration order upfront — a common interview strategy is "write recursive brute force → add memoization → convert to tabulation if space matters."
- This exact pattern (overlapping subproblems + optimal substructure) is what defines when DP applies at all — if subproblems don't overlap, plain recursion/divide-and-conquer is already optimal (e.g. merge sort).
- `long` (not `int`) matters for larger `n` — Fibonacci grows fast enough to overflow a 32-bit int around n≈47.

## Related

- See also: knapsack-01, coin-change
