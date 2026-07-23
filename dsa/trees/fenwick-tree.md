# Fenwick Tree (Binary Indexed Tree)

## Intuition

Like a segment tree, a Fenwick tree supports range-sum queries and point updates in O(log n) — but does it with a single flat array and clever bit manipulation instead of an explicit tree structure, giving a smaller memory footprint and simpler code. It exploits the binary representation of indices: each index is responsible for summing a specific range determined by its lowest set bit.

## Definition / How it Works

Store a 1-indexed array `tree[1..n]`. Each `tree[i]` holds the sum of a range ending at `i`, whose length is determined by `i`'s lowest set bit (`i & -i`).

- **Update(i, delta)**: add `delta` to `tree[i]`, then move to the next index that also needs updating: `i += (i & -i)` — this walks _up_ toward the root, touching all ranges that include index `i`. Repeat until `i > n`.
- **Query(i)** — prefix sum `[1, i]`: sum `tree[i]`, then move to the previous relevant index: `i -= (i & -i)` — this walks _down_, accumulating partial sums. Repeat until `i == 0`.
- **Range query [l, r]**: `query(r) - query(l-1)` — standard prefix-sum-difference trick.

The `i & -i` operation isolates the lowest set bit — it's what makes each update/query touch only O(log n) indices instead of O(n).

## Code

```java
class FenwickTree {
    int[] tree;
    int n;

    FenwickTree(int n) {
        this.n = n;
        tree = new int[n + 1]; // 1-indexed
    }

    void update(int i, int delta) {
        for (; i <= n; i += i & (-i)) {
            tree[i] += delta;
        }
    }

    int query(int i) { // prefix sum [1, i]
        int sum = 0;
        for (; i > 0; i -= i & (-i)) {
            sum += tree[i];
        }
        return sum;
    }

    int rangeQuery(int l, int r) {
        return query(r) - query(l - 1);
    }
}
```

## Example Problem

**Input:** array `[3, 2, -1, 6, 5, 4, -3, 3]` (1-indexed positions 1–8), build via repeated `update`, then query prefix sum `[1, 5]`.

## Trace

**Update(1, 3)** — add 3 at index 1: `i=1 (binary 0001)`, lowest set bit=1 → touches index 1, then `i += 1 = 2`, touches index 2, then `i += 2 = 4`, touches index 4, then `i += 4 = 8`, touches index 8, then `i=16 > n=8`, stop.
So inserting at index 1 updates `tree[1], tree[2], tree[4], tree[8]`.

**Query(5)** — prefix sum `[1,5]`: `i=5 (binary 0101)`, lowest set bit=1 → add `tree[5]`, `i -= 1 = 4`, lowest set bit=4 → add `tree[4]`, `i -= 4 = 0`, stop.
So `query(5) = tree[5] + tree[4]` — only 2 array accesses to get the sum of 5 elements, instead of summing all 5 directly.

| Operation     | Indices touched | Why                                                                                    |
| ------------- | --------------- | -------------------------------------------------------------------------------------- |
| update(1, +3) | 1, 2, 4, 8      | each index's range includes position 1                                                 |
| query(5)      | 5, 4            | tree[5] covers just position 5; tree[4] covers positions 1-4; together = positions 1-5 |

**Result:** both operations run in O(log n) ≈ O(log 8) = 3 steps max, regardless of array size.

## Complexity

- Update: O(log n)
- Query (prefix sum): O(log n)
- Range query: O(log n) (two prefix queries)
- Space: O(n) — just one array, smaller constant factor than segment tree's `4n`

## Key Points / Gotchas

- Must be **1-indexed** — `i & -i` breaks at index 0 (would loop forever), so Fenwick trees conventionally shift all positions by +1.
- Simpler and more memory-efficient than a segment tree, but less flexible — naturally supports only **invertible** operations like sum (since range query relies on subtraction: `query(r) - query(l-1)`). Doesn't directly support min/max (no inverse operation) without extra tricks.
- `i & -i` (two's complement trick to isolate lowest set bit) is worth memorizing — it's the one line that makes the whole structure work.
- Building from scratch: calling `update()` n times is O(n log n); there's an O(n) direct-build method too, but O(n log n) is usually fine and simpler to write correctly.

## Related

- See also: segment-tree
