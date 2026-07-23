# Graph BFS

## Intuition

BFS explores a graph outward in expanding "rings" from a start node — all nodes at distance 1 first, then all at distance 2, and so on. Because it explores in strictly increasing distance order, the first time BFS reaches any node is guaranteed to be via a shortest path (in terms of number of edges, for unweighted graphs).

## Definition / How it Works

1. Use a queue (FIFO) and a `visited` set. Enqueue the start node, mark it visited.
2. While the queue isn't empty: dequeue a node, process it, then enqueue all of its unvisited neighbors, marking each as visited **at the time of enqueueing** (not when dequeued — this avoids adding the same node to the queue multiple times).
3. Continue until the queue is empty.

Marking visited at enqueue time (not dequeue time) is the detail most people get wrong — without it, a node with multiple incoming edges from the current frontier gets enqueued multiple times.

## Code

```java
void bfs(int start, Map<Integer, List<Integer>> adj) {
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    queue.offer(start);
    visited.add(start);
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        for (int neighbor : adj.getOrDefault(node, List.of())) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);       // mark at enqueue time
                queue.offer(neighbor);
            }
        }
    }
}
```

## Example Problem

**Graph:** `1-2, 1-3, 2-4, 3-4, 4-5`
**Goal:** BFS traversal starting from node 1.

## Trace

| Step | Dequeue | Neighbors checked         | Newly enqueued | Queue after |
| ---- | ------- | ------------------------- | -------------- | ----------- |
| 1    | 1       | 2, 3                      | 2, 3           | [2, 3]      |
| 2    | 2       | 1(visited), 4             | 4              | [3, 4]      |
| 3    | 3       | 1(visited), 4(visited)    | —              | [4]         |
| 4    | 4       | 2(visited), 3(visited), 5 | 5              | [5]         |
| 5    | 5       | 4(visited)                | —              | []          |

**Result:** traversal order `1, 2, 3, 4, 5` — nodes visited in strictly increasing distance from node 1 (distance 1: {2,3}, distance 2: {4}, distance 3: {5}).

## Complexity

- Time: O(V + E) — every vertex and edge examined once
- Space: O(V) — visited set and queue

## Key Points / Gotchas

- Use BFS specifically when you need **shortest path in an unweighted graph** or **minimum number of steps/moves** — DFS can't guarantee this.
- Mark visited at enqueue time, not dequeue time — otherwise duplicate enqueues waste time and can cause incorrect distance tracking.
- To track actual distances, store a `dist[]` array (or level) alongside, updating it when a neighbor is first enqueued: `dist[neighbor] = dist[node] + 1`.
- For weighted graphs, plain BFS doesn't give shortest paths — need Dijkstra's or Bellman-Ford instead.

## Related

- See also: dfs, dijkstra
