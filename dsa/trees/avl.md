# AVL Tree

## Intuition

A plain BST can degenerate into a linked list (O(n) operations) if data is inserted in sorted order. An AVL tree fixes this by **self-balancing**: after every insert/delete, it checks whether the tree became too lopsided and, if so, performs rotations to restore balance — guaranteeing O(log n) height (and therefore O(log n) operations) no matter the insertion order.

## Definition / How it Works

Every node tracks a **balance factor** = `height(left subtree) - height(right subtree)`. The AVL invariant: balance factor must be in `{-1, 0, 1}` for every node. If an insert/delete pushes a node's balance factor to `-2` or `+2`, rotations restore balance:

- **Left-Left case** (balance +2, left child also left-heavy): single **right rotation**.
- **Right-Right case** (balance -2, right child also right-heavy): single **left rotation**.
- **Left-Right case** (balance +2, left child is right-heavy): left rotation on the left child, then right rotation on the node.
- **Right-Left case** (balance -2, right child is left-heavy): right rotation on the right child, then left rotation on the node.

After inserting a new node (standard BST insert), walk back up the recursion, updating heights and checking balance factors at each ancestor — fix the _first_ unbalanced node found (rotations there restore balance for the whole path).

## Code

```java
class Node {
    int val, height = 1;
    Node left, right;
    Node(int val) { this.val = val; }
}

int height(Node n) { return n == null ? 0 : n.height; }
int balanceFactor(Node n) { return n == null ? 0 : height(n.left) - height(n.right); }

Node rightRotate(Node y) {
    Node x = y.left;
    Node T2 = x.right;
    x.right = y;
    y.left = T2;
    y.height = Math.max(height(y.left), height(y.right)) + 1;
    x.height = Math.max(height(x.left), height(x.right)) + 1;
    return x; // new subtree root
}

Node leftRotate(Node x) {
    Node y = x.right;
    Node T2 = y.left;
    y.left = x;
    x.right = T2;
    x.height = Math.max(height(x.left), height(x.right)) + 1;
    y.height = Math.max(height(y.left), height(y.right)) + 1;
    return y; // new subtree root
}

Node insert(Node node, int val) {
    if (node == null) return new Node(val);
    if (val < node.val) node.left = insert(node.left, val);
    else if (val > node.val) node.right = insert(node.right, val);
    else return node;

    node.height = 1 + Math.max(height(node.left), height(node.right));
    int bf = balanceFactor(node);

    if (bf > 1 && val < node.left.val) return rightRotate(node);              // LL
    if (bf < -1 && val > node.right.val) return leftRotate(node);             // RR
    if (bf > 1 && val > node.left.val) { node.left = leftRotate(node.left); return rightRotate(node); }   // LR
    if (bf < -1 && val < node.right.val) { node.right = rightRotate(node.right); return leftRotate(node); } // RL

    return node;
}
```

## Example Problem

**Input:** insert `10, 20, 30` in order into an empty AVL tree.
**Goal:** show that the tree self-balances instead of becoming a skewed line.

## Trace

| Insert | Plain BST would do                                  | AVL does                                                                                                                                                                                                      |
| ------ | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10     | root = 10                                           | root = 10, height=1                                                                                                                                                                                           |
| 20     | 20 > 10 → right child                               | 20 > 10 → right child. Check node 10: bf = height(null) - height(20) = 0-1 = -1. Still within [-1,1], no rotation.                                                                                            |
| 30     | 30 > 20 → right child of 20 (skewed chain 10→20→30) | 30 > 20 → right child of 20. Walk back up: node 20 bf = 0-1=-1 (ok). Node 10 bf = 0 - height(20's subtree=2) = -2 → **unbalanced!** This is Right-Right case (30 > 20) → single **left rotation** at node 10. |

**Rotation result:** `leftRotate(10)` — 20 becomes new subtree root, 10 becomes its left child, 30 stays right child of 20.

```
Before rotation:        After left rotation:
10                             20
  \                           /  \
   20                       10    30
     \
      30
```

**Result:** balanced tree of height 2 instead of a degenerate chain of height 3 — search/insert stays O(log n).

## Complexity

- Search / Insert / Delete: O(log n) guaranteed worst case (height is always O(log n) by the balance invariant)
- Rotation: O(1) per rotation, at most O(log n) rotations total per insert/delete (usually just 1-2 in practice)
- Space: O(n), plus O(1) extra per node for the height field

## Key Points / Gotchas

- The **guarantee** is the whole point — AVL gives worst-case O(log n) where plain BST gives worst-case O(n). This matters anywhere adversarial or sorted input is possible.
- AVL is more strictly balanced than Red-Black trees (tighter balance factor), which means **faster lookups** but **more rotations on insert/delete** — AVL suits read-heavy workloads, Red-Black suits write-heavy ones (this is a common "compare the two" interview question).
- Always update `height` **before** computing `balanceFactor` in the insert function — using a stale height is a common bug.
- Identify LL/RR/LR/RL by comparing the new value to both the unbalanced node and its heavy child — don't memorize rotation code without understanding which case triggered it.

## Related

- See also: bst, tree-traversal-dfs
