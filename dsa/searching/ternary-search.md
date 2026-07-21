# Ternary Search

## Intuition

Instead of splitting the search space into 2 parts like binary search, split it into 3 parts using two midpoints. Mainly useful not for plain lookup (binary search is already optimal there) but for finding the maximum/minimum of a **unimodal function** — one that strictly increases then strictly decreases (or vice versa).

## Definition / How it Works

For finding a max in a unimodal function over `[low, high]`:

1. Compute `mid1 = low + (high - low) / 3`, `mid2 = high - (high - low) / 3`.
2. Compare `f(mid1)` and `f(mid2)`.
3. If `f(mid1) < f(mid2)`, the max can't be in `[low, mid1]` → discard it, set `low = mid1 + 1`.
4. Else, the max can't be in `[mid2, high]` → discard it, set `high = mid2 - 1`.
5. Repeat until the range converges.

## Code

```java
double ternarySearchMax(double low, double high, Function<Double, Double> f) {
    double eps = 1e-9;
    while (high - low > eps) {
        double mid1 = low + (high - low) / 3;
        double mid2 = high - (high - low) / 3;
        if (f.apply(mid1) < f.apply(mid2)) low = mid1;
        else high = mid2;
    }
    return f.apply((low + high) / 2);
}
```

## Example Problem

**Input:** `f(x) = -(x - 5)²+ 20` (a downward parabola, peak at x = 5), search range `[0, 10]`
**Goal:** find x that maximizes f(x).

## Trace

| Step | low              | high | mid1 | mid2 | f(mid1) | f(mid2) | action                              |
| ---- | ---------------- | ---- | ---- | ---- | ------- | ------- | ----------------------------------- |
| 1    | 0                | 10   | 3.33 | 6.67 | 17.2    | 17.2    | tie → high = mid2 = 6.67            |
| 2    | 0                | 6.67 | 2.22 | 4.44 | 12.3    | 19.7    | f(mid1)<f(mid2) → low = mid1 = 2.22 |
| 3    | 2.22             | 6.67 | 3.7  | 5.19 | 18.3    | 19.96   | low = mid1 = 3.7                    |
| ...  | narrows toward 5 |      |      |      |         |         | converges to peak ≈ 5.0             |

**Result:** converges to `x ≈ 5`, where `f(x) = 20` (the true maximum), after O(log₃ n) iterations.

## Complexity

- Time: O(log₃ n) for the search — same order as binary search's O(log₂ n) (constant factor difference only, both are O(log n))
- Space: O(1)

## Key Points / Gotchas

- **Not** faster than binary search for plain "find target in sorted array" — it makes 2 comparisons per iteration vs binary search's 1, so it's actually slightly worse for that use case. Its real value is unimodal function optimization.
- Requires strict unimodality — if the function is flat over some region or has multiple peaks, ternary search can converge to the wrong point.
- Common use: optimization problems in competitive programming (minimize cost function, maximize area, etc.) where you can evaluate f(x) but have no closed-form derivative.
- Don't confuse with ternary search **tree** (a completely different data structure for string storage).

## Related

- See also: binary-search
