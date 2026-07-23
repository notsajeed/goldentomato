# Minimum Spanning Tree (Kruskal's & Prim's)

## Intuition

Given a connected, weighted, undirected graph, a spanning tree connects all vertices using exactly `V-1` edges with no cycles. A **minimum** spanning tree (MST) is the one with the smallest total edge weight — think "cheapest way to connect all cities with roads." Two classic greedy algorithms solve this optimally: **Kruskal's** (sort edges, add cheapest ones that don't form a cycle) and **Prim's** (grow a single tree outward, always adding the cheapest edge that connects a new vertex).

## Definition / How it Works

**Kruskal's** (edge-focused):

1. Sort all edges by weight, ascending.
2. Use a Union-Find (Disjoint Set Union) structure to track connected components.
3. For each edge `(u, v, w)` in sorted order: if `u` and `v` are in different components (adding this edge won't form a cycle), add it to the MST and union their components. Otherwise skip it.
4. Stop once `V-1` edges are added.

**Prim's** (vertex-focused):

1. Start from any vertex, add it to the MST set.
2. Use a min-heap of edges crossing the boundary (MST set ↔ rest of graph). Repeatedly pop the cheapest crossing edge; if it connects to a vertex not yet in the MST, add that vertex and its edge, then push its new crossing edges.
3. Repeat until all vertices are included.

## Code

```java
// Kruskal's using Union-Find
int kruskalMST(int V, List<int[]> edges) { // edges: [u, v, weight]
    edges.sort((a, b) -> a[2] - b[2]);
    int[] parent = new int[V];
    for (int i = 0; i < V; i++) parent[i] = i;

    int totalWeight = 0, edgesUsed = 0;
    for (int[] edge : edges) {
        int u = find(parent, edge[0]), v = find(parent, edge[1]);
        if (u != v) {
            parent[u] = v;
            totalWeight += edge[2];
            edgesUsed++;
            if (edgesUsed == V - 1) break;
        }
    }
    return totalWeight;
}

int find(int[] parent, int x) {
    if (parent[x] != x) parent[x] = find(parent, parent[x]); // path compression
    return parent[x];
}
```

## Example Problem

**Graph (undirected, weighted):** edges `A-B(1), B-C(3), A-C(4), C-D(2), B-D(5)`
**Goal:** find MST using Kruskal's.

## Trace

**Sorted edges:** A-B(1), C-D(2), B-C(3), A-C(4), B-D(5)

| Edge    | find(u), find(v)       | Same component? | Action                     | MST edges so far |
| ------- | ---------------------- | --------------- | -------------------------- | ---------------- |
| A-B (1) | A, B                   | no              | add, union(A,B)            | {A-B}            |
| C-D (2) | C, D                   | no              | add, union(C,D)            | {A-B, C-D}       |
| B-C (3) | {A,B}, {C,D}           | no              | add, union → all connected | {A-B, C-D, B-C}  |
| A-C (4) | all same component now | yes             | skip (would form cycle)    | (unchanged)      |
| B-D (5) | all same component     | yes             | skip                       | (unchanged)      |

**Result:** MST = `{A-B(1), C-D(2), B-C(3)}`, total weight = **6**, using exactly `V-1 = 3` edges for 4 vertices — stopped early once enough edges were added.

## Complexity

- Kruskal's: O(E log E) — dominated by sorting edges; Union-Find operations are nearly O(1) with path compression + union by rank
- Prim's: O(E log V) with a binary heap
- Space: O(V + E)

## Key Points / Gotchas

- **Kruskal's vs Prim's**: Kruskal's is simpler and better for sparse graphs (few edges); Prim's (with a heap) is better for dense graphs. Both give the same total weight — MST is unique in total weight if all edge weights are distinct (the specific edge set can vary with ties).
- Path compression + union by rank in Union-Find is what keeps Kruskal's near-linear — without them, Union-Find degrades toward O(V) per operation.
- MST only makes sense for **connected** graphs — if the graph is disconnected, you get a "minimum spanning forest" instead (Kruskal's naturally handles this by just adding fewer than V-1 edges).
- Common real-world framing: network design (minimum cable to connect all offices), clustering (removing the most expensive MST edges splits data into clusters).

## Related

- See also: dijkstra
