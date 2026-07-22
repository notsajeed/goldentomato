# Binary Search Tree (BST)

## Intuition

A BST layers the "discard half the search space" idea of binary search onto a tree structure. Every node enforces an invariant: everything in its left subtree is smaller, everything in its right subtree is larger. This means search, insert, and delete can all skip entire subtrees at each step — O(log n) on average, same reasoning as binary search on a sorted array, but supporting O(log n) insert/delete too (which a sorted array can't do efficiently).

## Definition / How it Works

**BST property**: for every node, `left subtree values < node.val < right subtree values`.

- **Search**: compare target to current node; go left if smaller, right if larger, until found or you hit `null`.
- **Insert**: same traversal logic as search, but when you hit `null`, that's where the new node goes.
- **Delete**: three cases —
  1. Leaf node → just remove it.
  2. One child → replace the node with its child.
  3. Two children → replace the node's value with its **in-order successor** (smallest value in right subtree, i.e. leftmost node of right subtree), then delete that successor node (which has at most one child, reducing to case 1 or 2).

## Code

```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

TreeNode insert(TreeNode node, int val) {
    if (node == null) return new TreeNode(val);
    if (val < node.val) node.left = insert(node.left, val);
    else if (val > node.val) node.right = insert(node.right, val);
    return node; // val == node.val: no duplicates inserted
}

boolean search(TreeNode node, int val) {
    if (node == null) return false;
    if (node.val == val) return true;
    return val < node.val ? search(node.left, val) : search(node.right, val);
}
```

## Example Problem

**Input:** insert values `5, 3, 8, 1, 4` into an empty BST, then search for `4`.
**Goal:** show resulting tree shape and the search path.

## Trace

**Insertions:**
| Insert | Path taken | Tree after |
|---|---|---|
| 5 | root empty → becomes root | 5 |
| 3 | 3 < 5 → go left → null → insert | 5 (left=3) |
| 8 | 8 > 5 → go right → null → insert | 5 (left=3, right=8) |
| 1 | 1 < 5 → left(3) → 1 < 3 → left → null → insert | 3 gets left child 1 |
| 4 | 4 < 5 → left(3) → 4 > 3 → right → null → insert | 3 gets right child 4 |

Final tree:

```
        5
       / \
      3   8
     / \
    1   4
```

**Search for 4:** start at 5 → `4 < 5` go left to 3 → `4 > 3` go right to 4 → match, return `true`. 2 comparisons instead of scanning all 5 elements.

## Complexity

- Search / Insert / Delete: O(log n) average (balanced tree), O(n) worst case (skewed tree, e.g. inserting sorted data 1,2,3,4,5 in order — degenerates into a linked list)
- Space: O(n) for the tree, O(h) recursion stack for operations

## Key Points / Gotchas

- **Worst case matters**: a plain BST gives no balance guarantee — inserting already-sorted data produces a degenerate O(n)-depth tree, losing all the log n benefit. This is exactly why AVL/Red-Black trees exist.
- In-order traversal of a BST always produces sorted output — useful for validating "is this a valid BST?" (values must be strictly increasing in-order).
- Delete's two-children case (replace with in-order successor) is the trickiest to code correctly — practice it explicitly, it's a very common interview ask.
- Duplicates: decide a convention up front (disallow, or always go right/left for equal values) — inconsistent handling is a common bug source.

## Related

- See also: avl, tree-traversal-dfs
