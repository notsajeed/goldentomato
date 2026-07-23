# Strongly Connected Components (Kosaraju's Algorithm)

## Intuition

In a directed graph, a **strongly connected component (SCC)** is a maximal group of vertices where every vertex can reach every other vertex in the group via directed paths. Kosaraju's algorithm finds all SCCs cleverly using two DFS passes and a neat trick: the order in which nodes _finish_ in a DFS on the original graph, combined with a DFS on the **reversed** graph, correctly isolates each SCC.

## Definition / How it Works

1. **First DFS pass** on the original graph: run DFS from every unvisited node, and push each node onto a stack **when it finishes** (post-order) — same finishing-order idea as topological sort.
2. **Reverse all edges** of the graph (transpose).
3. **Second DFS pass** on the reversed graph: pop nodes off the stack one at a time (highest finish time first). For each unvisited node popped, run DFS on the reversed graph — everything reached in this single DFS call forms one complete SCC.

Why this works (intuition, not full proof): the node that finishes last in pass 1 must be in a "source" SCC (or on a path from one) in the condensation graph. Running DFS from it on the _reversed_ graph confines the traversal to exactly that SCC, since edges leaving that SCC in the original graph become edges entering it in the reverse — they can't be used to escape further.

## Code

```java
List<List<Integer>> kosaraju(int V, Map<Integer, List<Integer>> adj) {
    Deque<Integer> finishStack = new ArrayDeque<>();
    boolean[] visited = new boolean[V];

    // Pass 1: fill stack by finish order
    for (int i = 0; i < V; i++) {
        if (!visited[i]) fillOrder(i, adj, visited, finishStack);
    }

    // Reverse graph
    Map<Integer, List<Integer>> reversed = reverseGraph(V, adj);

    // Pass 2: DFS on reversed graph in stack order
    Arrays.fill(visited, false);
    List<List<Integer>> sccs = new ArrayList<>();
    while (!finishStack.isEmpty()) {
        int node = finishStack.pop();
        if (!visited[node]) {
            List<Integer> component = new ArrayList<>();
            dfsCollect(node, reversed, visited, component);
            sccs.add(component);
        }
    }
    return sccs;
}

void fillOrder(int node, Map<Integer, List<Integer>> adj, boolean[] visited, Deque<Integer> stack) {
    visited[node] = true;
    for (int neighbor : adj.getOrDefault(node, List.of())) {
        if (!visited[neighbor]) fillOrder(neighbor, adj, visited, stack);
    }
    stack.push(node); // push on finish
}

void dfsCollect(int node, Map<Integer, List<Integer>> adj, boolean[] visited, List<Integer> component) {
    visited[node] = true;
    component.add(node);
    for (int neighbor : adj.getOrDefault(node, List.of())) {
        if (!visited[neighbor]) dfsCollect(neighbor, adj, visited, component);
    }
}
```

## Example Problem

**Graph (directed):** `0→1, 1→2, 2→0, 1→3, 3→4`
(nodes 0,1,2 form a cycle → one SCC; 3 and 4 are each their own SCC)

## Trace

**Pass 1 (DFS from 0, fill finish order):**

- dfs(0) → visit 0 → dfs(1) → visit 1 → dfs(2) → visit 2 → dfs(0) already visited → 2 finishes, push 2 → back to 1, next neighbor 3 → dfs(3) → visit 3 → dfs(4) → visit 4, no neighbors, finishes, push 4 → back to 3, finishes, push 3 → back to 1, finishes, push 1 → back to 0, finishes, push 0

**Finish stack (top to bottom):** `[0, 1, 3, 4, 2]`

**Reversed graph edges:** `1→0, 2→1, 0→2, 3→1, 4→3`

**Pass 2** (pop stack, DFS on reversed graph):
| Pop | Visited already? | DFS on reversed graph from here | SCC found |
|---|---|---|---|
| 0 | no | 0→2 (reversed edge)→1 (reversed edge)→0(visited) | {0, 2, 1} |
| 1 | yes (in above) | skip | — |
| 3 | no | 3→1(visited), no other unvisited neighbors | {3} |
| 4 | no | 4→3(visited) | {4} |
| 2 | yes | skip | — |

**Result:** SCCs = `{0, 1, 2}`, `{3}`, `{4}` — correctly isolates the cycle as one component, with 3 and 4 as trivial single-node SCCs.

## Complexity

- Time: O(V + E) — two DFS passes plus graph reversal, all linear
- Space: O(V + E) — reversed graph, visited arrays, stack

## Key Points / Gotchas

- Kosaraju's requires **two full DFS passes** and a graph reversal — Tarjan's algorithm finds SCCs in a **single** DFS pass using low-link values, which is more efficient in practice despite the same O(V+E) complexity, but is trickier to implement correctly.
- The **condensation graph** (collapsing each SCC into a single node) is always a DAG — this is what makes the finish-time trick work, and it's a useful fact for follow-up problems (e.g. "minimum edges to make the graph strongly connected").
- Common use: detecting cycles in dependency graphs, analyzing web page link structure (SCCs of hyperlinks), compiler analysis (mutually recursive function groups).
- A graph is fully strongly connected (single SCC covering all nodes) if and only if Kosaraju's produces exactly one component.

## Related

- See also: dfs, topo-sort
