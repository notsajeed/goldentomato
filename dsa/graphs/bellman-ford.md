# Bellman-Ford Algorithm

## Intuition

Dijkstra's greedy approach breaks with negative edge weights. Bellman-Ford takes a slower but more robust approach: instead of greedily finalizing nodes, it simply relaxes **every** edge, repeatedly, `V-1` times. After `V-1` rounds, every shortest path (which can have at most `V-1` edges in a graph with V vertices, since a shortest path never revisits a node) is guaranteed to be found — no matter the weight signs. A bonus: a `V`-th round that still finds improvements means there's a negative-weight cycle reachable from the source.

## Definition / How it Works

1. Initialize `dist[start] = 0`, all others = infinity.
2. Repeat `V - 1` times: for every edge `(u, v, weight)` in the graph, if `dist[u] + weight < dist[v]`, update `dist[v] = dist[u] + weight`.
3. **Negative cycle check**: run one more pass over all edges. If any edge can still be relaxed, a negative-weight cycle exists reachable from the source (shortest paths aren't well-defined).

Why `V - 1` rounds is enough: each round guarantees the shortest path using at most that many edges is found; since the longest possible simple shortest path uses `V-1` edges, `V-1` rounds suffice to propagate the shortest distance to every node.

## Code

```java
int[] bellmanFord(int start, int V, List<int[]> edges) { // edges: [u, v, weight]
    int[] dist = new int[V];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[start] = 0;

    for (int i = 0; i < V - 1; i++) {
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    // Negative cycle check
    for (int[] edge : edges) {
        int u = edge[0], v = edge[1], w = edge[2];
        if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
            throw new IllegalStateException("Negative weight cycle detected");
        }
    }
    return dist;
}
```

## Example Problem

**Graph (directed):** edges `0→1 (4), 0→2 (5), 1→2 (-3), 2→3 (2)`, V=4 nodes.
**Goal:** shortest distances from node 0.

## Trace

Init: `dist = [0, ∞, ∞, ∞]`

**Round 1** (process edges in order 0→1, 0→2, 1→2, 2→3):
| Edge | Check | dist[] after |
|---|---|---|
| 0→1 (4) | dist[0]+4=4 < ∞ | [0,4,∞,∞] |
| 0→2 (5) | dist[0]+5=5 < ∞ | [0,4,5,∞] |
| 1→2 (-3) | dist[1]-3=1 < 5 | [0,4,1,∞] |
| 2→3 (2) | dist[2]+2=3 < ∞ | [0,4,1,3] |

**Round 2** (V-1=3, so 2 more rounds — but check if anything changes):
| Edge | Check | Change? |
|---|---|---|
| 0→1 | 0+4=4, not < 4 | no |
| 0→2 | 0+5=5, not < 1 | no |
| 1→2 | 4-3=1, not < 1 | no |
| 2→3 | 1+2=3, not < 3 | no |

No changes — already converged after round 1 (fewer rounds needed than the worst-case bound in this small example). Rounds 2 and 3 confirm stability.

**Negative cycle check:** re-run all edges once more — no further improvement found, so no negative cycle.

**Result:** `dist = [0, 4, 1, 3]` — correctly found the shorter path `0→1→2` (4-3=1) over the direct `0→2` (5), something Dijkstra's greedy approach could get wrong in the presence of negative edges.

## Complexity

- Time: O(V × E) — V-1 rounds, each examining every edge
- Space: O(V) for the distance array

## Key Points / Gotchas

- Strictly slower than Dijkstra's (O(VE) vs O((V+E) log V)) — only reach for Bellman-Ford when negative weights are possible, or when negative-cycle **detection** is itself the goal.
- The negative-cycle check (one extra round) is a common thing to forget — without it, the algorithm silently returns wrong "shortest" distances when a negative cycle exists (since shortest paths through a negative cycle are technically `-infinity`).
- Order of edge processing within a round doesn't affect correctness (it may affect how many rounds are actually needed to converge, as seen in the trace above, but the guarantee is still V-1 rounds worst case).
- Also used in distributed systems as the basis for distance-vector routing protocols (e.g. early RIP) — good context to mention if asked about real-world applications.

## Related

- See also: dijkstra, floyd-warshall
