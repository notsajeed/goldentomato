# Tree Traversal — BFS (Level Order)

## Intuition

BFS visits a tree level by level, left to right, before moving to the next level — like reading a book page by page rather than jumping into one paragraph and following it deep. This "breadth-first" order is exactly what you need when the answer depends on level/depth (level averages, shortest path in an unweighted tree, printing level by level), and it's the tree specialization of the general graph BFS pattern.

## Definition / How it Works

Unlike DFS, BFS isn't naturally recursive — it needs a **queue** to remember which nodes to visit next, in the order they were discovered (FIFO).

1. Push the root into the queue.
2. While the queue isn't empty:
   - Dequeue a node, process/visit it.
   - Enqueue its children (left, then right) so they're processed after all nodes currently in the queue.
3. To track levels explicitly, snapshot the queue's size at the start of each iteration — everything currently in the queue belongs to the same level.

## Code

```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
        int levelSize = queue.size(); // nodes belonging to this level
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < levelSize; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        result.add(level);
    }
    return result;
}
```

## Example Problem

**Input:**

```
        3
       / \
      9   20
         /  \
        15   7
```

**Goal:** return level-order traversal as `[[3], [9,20], [15,7]]`.

## Trace

| Iteration | levelSize | Queue at start | Nodes processed | Children enqueued           | result so far       |
| --------- | --------- | -------------- | --------------- | --------------------------- | ------------------- |
| 1         | 1         | [3]            | 3               | 9, 20                       | [[3]]               |
| 2         | 2         | [9, 20]        | 9, 20           | 15, 7 (from 20; 9 has none) | [[3],[9,20]]        |
| 3         | 2         | [15, 7]        | 15, 7           | none                        | [[3],[9,20],[15,7]] |

**Result:** `[[3], [9, 20], [15, 7]]` — queue empties after 3 iterations.

## Complexity

- Time: O(n) — every node visited once
- Space: O(n) — worst case the queue holds an entire level, which for a balanced tree can be up to ~n/2 nodes at the widest level

## Key Points / Gotchas

- Snapshotting `queue.size()` before the inner loop is the key trick for level-by-level grouping — without it you'd get a flat list, not grouped levels.
- BFS is the natural choice for "minimum depth" / "shortest path to a target node" in an unweighted tree — first time you reach the target is guaranteed shortest, unlike DFS which might find a longer path first.
- Don't confuse with DFS pre-order — pre-order visits root, then fully explores left subtree, then right; BFS interleaves across the whole level first.
- Java's `Queue<TreeNode> queue = new LinkedList<>()` is the idiomatic choice here (or `ArrayDeque` for better performance).

## Related

- See also: tree-traversal-dfs, bst
