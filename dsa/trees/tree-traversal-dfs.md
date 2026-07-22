# Tree Traversal — DFS (Pre/In/Post-order)

## Intuition

DFS dives as deep as possible down one branch before backtracking, rather than sweeping across levels. A tree's recursive structure (a node plus a left and right subtree, each also a tree) makes DFS the natural fit — it can be written recursively in almost the same shape as the tree's own definition. The three orderings (pre, in, post) differ only in _when_ you process the current node relative to recursing into its children.

## Definition / How it Works

- **Pre-order** (root → left → right): process the node **before** recursing — useful for copying/serializing a tree, since you record structure top-down.
- **In-order** (left → root → right): process the node **between** the two recursive calls — for a BST, this visits nodes in **sorted ascending order**, which is its main use.
- **Post-order** (left → right → root): process the node **after** both recursive calls — useful when children must be fully handled before the parent (e.g. deleting a tree, computing subtree sizes/heights bottom-up).

All three share the same recursive skeleton; only the position of the "visit" line changes.

## Code

```java
void preorder(TreeNode node, List<Integer> out) {
    if (node == null) return;
    out.add(node.val);           // visit BEFORE recursing
    preorder(node.left, out);
    preorder(node.right, out);
}

void inorder(TreeNode node, List<Integer> out) {
    if (node == null) return;
    inorder(node.left, out);
    out.add(node.val);           // visit BETWEEN recursive calls
    inorder(node.right, out);
}

void postorder(TreeNode node, List<Integer> out) {
    if (node == null) return;
    postorder(node.left, out);
    postorder(node.right, out);
    out.add(node.val);           // visit AFTER recursing
}
```

## Example Problem

**Input:**

```
        1
       / \
      2   3
     / \
    4   5
```

**Goal:** compute pre-order, in-order, and post-order traversals.

## Trace

**Pre-order** (visit before recursing): call order is `1 → 2 → 4 → 5 → 3`
| Call | Action |
|---|---|
| preorder(1) | visit 1 → recurse left(2) |
| preorder(2) | visit 2 → recurse left(4) |
| preorder(4) | visit 4 → both children null, return |
| (back to 2) | recurse right(5) → visit 5 → return |
| (back to 1) | recurse right(3) → visit 3 → return |

**Result:** Pre-order = `[1, 2, 4, 5, 3]`
**In-order** = `[4, 2, 5, 1, 3]` (left subtree fully, then 1, then right subtree)
**Post-order** = `[4, 5, 2, 3, 1]` (children before parent, root always last)

## Complexity

- Time: O(n) — every node visited exactly once, for all three orderings
- Space: O(h) — recursion stack depth = tree height h; O(log n) for balanced tree, O(n) worst case for a skewed (linked-list-like) tree

## Key Points / Gotchas

- **In-order traversal of a BST always yields sorted order** — this is the single most-tested fact about DFS + BST combined; use it to validate a BST or find the kth smallest element.
- All three can be done iteratively with an explicit stack instead of recursion — required when recursion depth risks a stack overflow on very unbalanced trees.
- Post-order is what you want when deleting a tree node-by-node (free children before the parent) or computing any bottom-up aggregate (height, diameter, subtree sum).
- Don't memorize the orders by rote — derive them from "where does the visit line sit relative to the two recursive calls," it's less error-prone under interview pressure.

## Related

- See also: tree-traversal-bfs, bst
