# Segment Tree

## Intuition

Given an array, you often need repeated **range queries** (sum, min, max over `[l, r]`) mixed with **point updates**. A prefix-sum array answers range-sum queries in O(1) but breaks the moment you update an element (O(n) to rebuild). A segment tree answers both range queries and point updates in O(log n), by precomputing aggregates over nested ranges in a binary tree, so any range query only needs to combine O(log n) precomputed segments instead of touching every element.

## Definition / How it Works

A segment tree is a binary tree (usually stored in an array, like a heap) where:

- Each **leaf** represents a single array element.
- Each **internal node** represents the aggregate (sum, min, max, etc.) of its two children's ranges — recursively, of the range `[l, r]` it covers.
- The root covers the entire array `[0, n-1]`.

Stored as an array of size `4n` (safe upper bound for any n): node `i` has children `2i+1` and `2i+2`.

- **Build**: recursively split `[l, r]` into `[l, mid]` and `[mid+1, r]`, build each half, combine into the current node.
- **Query(ql, qr)**: if the current node's range is fully outside `[ql, qr]`, return identity (0 for sum). If fully inside, return this node's stored value directly. Otherwise, recurse into both children and combine.
- **Update(idx, val)**: recurse down to the leaf for `idx`, update it, then recompute every ancestor's aggregate on the way back up.

## Code

```java
class SegmentTree {
    int[] tree, arr;
    int n;

    SegmentTree(int[] input) {
        arr = input;
        n = input.length;
        tree = new int[4 * n];
        build(0, 0, n - 1);
    }

    void build(int node, int l, int r) {
        if (l == r) { tree[node] = arr[l]; return; }
        int mid = (l + r) / 2;
        build(2*node+1, l, mid);
        build(2*node+2, mid+1, r);
        tree[node] = tree[2*node+1] + tree[2*node+2]; // sum aggregate
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;              // no overlap
        if (ql <= l && r <= qr) return tree[node];    // total overlap
        int mid = (l + r) / 2;                          // partial overlap
        return query(2*node+1, l, mid, ql, qr) + query(2*node+2, mid+1, r, ql, qr);
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) { tree[node] = val; return; }
        int mid = (l + r) / 2;
        if (idx <= mid) update(2*node+1, l, mid, idx, val);
        else update(2*node+2, mid+1, r, idx, val);
        tree[node] = tree[2*node+1] + tree[2*node+2]; // recompute on the way up
    }
}
```

## Example Problem

**Input:** `arr = [1, 3, 5, 7, 9, 11]`
**Goal:** query sum of range `[1, 3]` (values 3+5+7 = 15), then update index 1 to 10, then re-query `[1, 3]`.

## Trace

**Build** produces a tree where the root covers `[0,5]` = sum 36, splitting down to leaves.

**Query [1,3]** starting at root `[0,5]`:
| Node range | Overlap with [1,3]? | Action |
|---|---|---|
| [0,5] | partial | recurse into [0,2] and [3,5] |
| [0,2] | partial | recurse into [0,1] and [2,2] |
| [0,1] | partial | recurse into [0,0] and [1,1] |
| [0,0] | none ([0,0] vs [1,3]) | return 0 |
| [1,1] | total (1 is in [1,3]) | return tree value = 3 |
| [2,2] | total | return 5 |
| [3,5] | partial | recurse into [3,4] and [5,5] |
| [3,4] | partial → [3,3] total=7, [4,4] none=0 | returns 7 |
| [5,5] | none | return 0 |

**Sum up:** 0 + 3 + 5 + 7 + 0 = **15** ✓ (matches 3+5+7)

**Update index 1 → 10:** leaf [1,1] becomes 10, then every ancestor on the path recomputes: [0,1]=1+10=11, [0,2]=11+5=16, [0,5]=16+7+9+11=43.

**Re-query [1,3]:** same traversal, now returns 0+10+5+7+0 = **22** — reflects the update, computed in O(log n) without rebuilding the whole tree.

## Complexity

- Build: O(n)
- Query: O(log n)
- Update: O(log n)
- Space: O(n) (the 4n array bound)

## Key Points / Gotchas

- The `4n` array size is a safe (slightly loose) upper bound for a segment tree stored this way — using exactly `2n` can overflow for non-power-of-2 sizes.
- Different aggregate functions (sum, min, max, gcd) all use the exact same structure — only the "combine" step (`tree[node] = ...`) changes.
- **Lazy propagation** extends this to support **range updates** (not just point updates) in O(log n) — defers updates to child nodes until they're actually queried. Know this exists even if not implementing it from scratch.
- Compare with Fenwick tree (BIT): segment tree is more general (supports min/max/gcd, range updates with lazy propagation) but uses more memory and has a larger constant factor; Fenwick tree is simpler and faster but naturally suited only to sum-like invertible operations.

## Related

- See also: fenwick-tree
