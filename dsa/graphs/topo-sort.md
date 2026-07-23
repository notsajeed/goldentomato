# Topological Sort

## Intuition

Given a **directed acyclic graph (DAG)** representing dependencies (e.g. "course B requires course A first"), a topological sort produces a linear ordering of all vertices such that every edge `u → v` has `u` appearing before `v`. It answers "in what order can I do these tasks, respecting all prerequisites?"

## Definition / How it Works

Two standard approaches:

**Kahn's algorithm (BFS-based)**:

1. Compute in-degree (number of incoming edges) for every node.
2. Enqueue all nodes with in-degree 0 (no prerequisites — can start immediately).
3. While the queue isn't empty: dequeue a node, add it to the result, then for each of its outgoing edges, decrement the neighbor's in-degree. If a neighbor's in-degree hits 0, enqueue it.
4. If the result contains all V nodes, it's a valid topological order. If fewer, the graph has a cycle (no valid ordering exists).

**DFS-based**: run DFS, and after fully exploring a node (post-order, all its descendants processed), push it onto a stack. Reverse the stack at the end — this works because a node with no remaining unexplored dependents naturally gets finished (and pushed) last among its ancestors.

## Code

```java
// Kahn's algorithm
List<Integer> topoSort(int V, Map<Integer, List<Integer>> adj) {
    int[] inDegree = new int[V];
    for (List<Integer> neighbors : adj.values()) {
        for (int v : neighbors) inDegree[v]++;
    }

    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < V; i++) if (inDegree[i] == 0) queue.offer(i);

    List<Integer> result = new ArrayList<>();
    while (!queue.isEmpty()) {
        int node = queue.poll();
        result.add(node);
        for (int neighbor : adj.getOrDefault(node, List.of())) {
            if (--inDegree[neighbor] == 0) queue.offer(neighbor);
        }
    }

    if (result.size() != V) throw new IllegalStateException("Graph has a cycle");
    return result;
}
```

## Example Problem

**Graph (course prerequisites):** `0→1, 0→2, 1→3, 2→3`
(0 = "Intro", 1 = "Data Structures", 2 = "Discrete Math", 3 = "Algorithms" — 3 needs both 1 and 2)

## Trace

**In-degrees:** node 0: 0, node 1: 1 (from 0), node 2: 1 (from 0), node 3: 2 (from 1 and 2)

**Initial queue:** [0] (only node with in-degree 0)

| Step | Dequeue | Add to result | Decrement neighbors      | Newly in-degree-0 | Queue after |
| ---- | ------- | ------------- | ------------------------ | ----------------- | ----------- |
| 1    | 0       | [0]           | 1→0 (was 1), 2→0 (was 1) | 1, 2              | [1, 2]      |
| 2    | 1       | [0,1]         | 3→1 (was 2)              | none (3 still 1)  | [2]         |
| 3    | 2       | [0,1,2]       | 3→0 (was 1)              | 3                 | [3]         |
| 4    | 3       | [0,1,2,3]     | none                     | —                 | []          |

**Result:** `[0, 1, 2, 3]` — a valid order: take Intro, then Data Structures and Discrete Math (either order), then Algorithms. `result.size() == 4 == V`, confirming no cycle.

## Complexity

- Time: O(V + E) — both Kahn's and DFS-based
- Space: O(V) — in-degree array, queue/stack

## Key Points / Gotchas

- **Multiple valid orderings usually exist** — a topological sort isn't unique unless the graph enforces a strict total order. Any ordering respecting all edges is correct.
- Kahn's naturally detects cycles: if `result.size() < V` at the end, some nodes never reached in-degree 0, meaning they're stuck in a cycle.
- Classic applications: build systems (compile order), course scheduling, task scheduling with dependencies, spreadsheet formula evaluation order.
- Only defined for **DAGs** — a cyclic graph has no valid topological order (there's no way to linearly order nodes that depend on each other circularly).

## Related

- See also: dfs, scc
