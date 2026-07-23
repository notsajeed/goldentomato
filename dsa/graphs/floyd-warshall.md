# Floyd-Warshall Algorithm

## Intuition

Dijkstra's and Bellman-Ford both find shortest paths from a **single source**. If you need shortest paths between **every pair** of nodes, running Dijkstra's from every node works (O(V × (V+E) log V)) but Floyd-Warshall offers a cleaner, purely dynamic-programming approach: incrementally allow paths to route "through" each node as an intermediate, one node at a time, updating the all-pairs distance matrix as you go.

## Definition / How it Works

Maintain a `dist[i][j]` matrix, initialized to the direct edge weight (or infinity if no edge, 0 if `i == j`).

For each node `k` from `1` to `V` (as a candidate intermediate node), for every pair `(i, j)`: check if routing through `k` improves the path — `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.

After considering all `V` nodes as possible intermediates, `dist[i][j]` holds the true shortest distance between every pair. The DP insight: `dist[i][j]` after processing intermediates `{1,...,k}` represents the shortest path using only those nodes as intermediates — by the time all `k` are processed, no restriction remains.

## Code

```java
int[][] floydWarshall(int[][] graph, int V) { // graph[i][j] = weight or INF if no edge
    int[][] dist = new int[V][V];
    for (int i = 0; i < V; i++) dist[i] = graph[i].clone();

    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE
                        && dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    return dist;
}
```

## Example Problem

**Graph (3 nodes, directed):** `0→1 (3), 1→2 (1), 0→2 (10)`
**Goal:** all-pairs shortest distances.

## Trace

**Initial matrix** (∞ = no direct edge, 0 on diagonal):

```
      0    1    2
0  [  0,   3,  10 ]
1  [  ∞,   0,   1 ]
2  [  ∞,   ∞,   0 ]
```

**k=0** (route through node 0): check if `dist[i][0] + dist[0][j] < dist[i][j]` for all i,j. Node 0 has no incoming edges (dist[1][0], dist[2][0] = ∞), so no improvements possible this round.

**k=1** (route through node 1): check `dist[i][1] + dist[1][j]`.

- `dist[0][2]`: current = 10. Via 1: `dist[0][1] + dist[1][2] = 3 + 1 = 4`. `4 < 10` → update `dist[0][2] = 4`.

Matrix after k=1:

```
      0    1    2
0  [  0,   3,   4 ]
1  [  ∞,   0,   1 ]
2  [  ∞,   ∞,   0 ]
```

**k=2** (route through node 2): node 2 has no outgoing edges, no improvements possible.

**Result:** `dist[0][2] = 4` (path 0→1→2), correctly beating the direct edge weight of 10 — found by allowing routing through intermediate node 1.

## Complexity

- Time: O(V³) — three nested loops over all vertices
- Space: O(V²) for the distance matrix

## Key Points / Gotchas

- O(V³) is fine for dense graphs with modest V (a few hundred nodes) but becomes impractical for large sparse graphs — in that case, running Dijkstra's from every source (O(V(V+E)logV)) is often faster.
- Works with negative edge weights (unlike Dijkstra's), but **not** with negative cycles — if `dist[i][i] < 0` after running, a negative cycle exists.
- The loop order matters critically: `k` must be the **outermost** loop — `dist[i][j]` must be finalized for intermediates `{1..k}` before considering `k+1`, or the DP invariant breaks.
- Simple to code correctly (three nested loops, one line of relaxation) — a strong choice in interviews/competitive programming when V is small and all-pairs distances are needed, purely for implementation simplicity.

## Related

- See also: dijkstra, bellman-ford
