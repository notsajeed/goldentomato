# Dijkstra's Algorithm

## Intuition

For shortest paths in a **weighted** graph (non-negative weights), plain BFS doesn't work — it counts edges, not weights. Dijkstra's greedily picks the unvisited node with the smallest known distance so far, finalizes it (since no shorter path to it can exist — any other path would have to go through a currently-larger-distance node), and relaxes (updates) its neighbors' distances. Repeat until all reachable nodes are finalized.

## Definition / How it Works

1. Initialize `dist[start] = 0`, all others = infinity. Use a min-heap (priority queue) keyed by distance.
2. Push `(0, start)` into the heap.
3. While the heap isn't empty: pop the node with smallest distance. If already finalized, skip (stale heap entry). Otherwise finalize it, and for each neighbor, if `dist[node] + weight(node, neighbor) < dist[neighbor]`, update `dist[neighbor]` and push `(newDist, neighbor)`.
4. When the heap empties, `dist[]` holds shortest distances from `start` to every reachable node.

The greedy correctness relies on **non-negative weights** — with negative weights, a node finalized early could later be beaten by a path through a "worse-looking" node, breaking the greedy assumption. That's exactly why Bellman-Ford exists for negative weights.

## Code

```java
int[] dijkstra(int start, int n, Map<Integer, List<int[]>> adj) { // adj: node -> list of [neighbor, weight]
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[start] = 0;
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]); // [distance, node]
    pq.offer(new int[]{0, start});
    boolean[] finalized = new boolean[n];

    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int d = curr[0], node = curr[1];
        if (finalized[node]) continue; // stale entry
        finalized[node] = true;
        for (int[] edge : adj.getOrDefault(node, List.of())) {
            int neighbor = edge[0], weight = edge[1];
            if (dist[node] + weight < dist[neighbor]) {
                dist[neighbor] = dist[node] + weight;
                pq.offer(new int[]{dist[neighbor], neighbor});
            }
        }
    }
    return dist;
}
```

## Example Problem

**Graph (weighted, directed):** `0→1 (4), 0→2 (1), 2→1 (2), 1→3 (1), 2→3 (5)`
**Goal:** shortest distances from node 0.

## Trace

Init: `dist = [0, ∞, ∞, ∞]`, heap = [(0,0)]

| Pop (dist,node) | finalized?            | Relax neighbors                                        | dist[] after | heap after                    |
| --------------- | --------------------- | ------------------------------------------------------ | ------------ | ----------------------------- |
| (0, 0)          | no → finalize 0       | 0→1: 0+4=4 < ∞ → dist[1]=4; 0→2: 0+1=1 < ∞ → dist[2]=1 | [0,4,1,∞]    | [(1,2),(4,1)]                 |
| (1, 2)          | no → finalize 2       | 2→1: 1+2=3 < 4 → dist[1]=3; 2→3: 1+5=6 < ∞ → dist[3]=6 | [0,3,1,6]    | [(3,1),(4,1)stale,(6,3)]      |
| (3, 1)          | no → finalize 1       | 1→3: 3+1=4 < 6 → dist[3]=4                             | [0,3,1,4]    | [(4,1)stale,(4,3),(6,3)stale] |
| (4, 1)          | **yes, skip** (stale) | —                                                      | —            | [(4,3),(6,3)]                 |
| (4, 3)          | no → finalize 3       | no outgoing edges                                      | [0,3,1,4]    | [(6,3)]                       |
| (6, 3)          | yes, skip             | —                                                      | —            | []                            |

**Result:** `dist = [0, 3, 1, 4]` — shortest path to node 1 is via node 2 (0→2→1 = 1+2 = 3), not the direct edge (0→1 = 4), which is exactly why the greedy relaxation matters.

## Complexity

- Time: O((V + E) log V) with a binary heap
- Space: O(V + E) — adjacency list, distance array, heap

## Key Points / Gotchas

- **Fails with negative edge weights** — the greedy "finalize smallest, never revisit" assumption breaks. Use Bellman-Ford instead if negative weights are possible.
- The `if (finalized[node]) continue;` stale-entry check is essential — Java's PriorityQueue has no efficient "decrease-key" operation, so outdated `(oldDist, node)` entries are simply skipped when popped later.
- To reconstruct the actual shortest path (not just distance), track a `parent[]` array, updated every time `dist[neighbor]` is improved.
- For dense graphs, an O(V²) array-based implementation (no heap) can outperform the heap version due to lower constant factor — a good "which approach and why" interview follow-up.

## Related

- See also: bellman-ford, mst, a-star
