# Graph DFS

## Intuition

DFS explores as far as possible down one path before backtracking — like exploring a maze by always taking the first available turn and only backing up when you hit a dead end. Unlike BFS's level-by-level breadth, DFS naturally suits problems about **structure and reachability** (does a path exist, is there a cycle, connected components) rather than shortest distance.

## Definition / How it Works

Two implementations, same core idea:

- **Recursive**: visit a node, mark it visited, recursively visit each unvisited neighbor. The call stack implicitly tracks the path.
- **Iterative**: use an explicit stack instead of recursion — push the start node, and while the stack isn't empty, pop a node, process it if not yet visited, then push its unvisited neighbors.

Both explore depth-first; the recursive version is usually cleaner to write but risks stack overflow on very deep/large graphs, where the iterative version is safer.

## Code

```java
// Recursive
void dfs(int node, Map<Integer, List<Integer>> adj, Set<Integer> visited) {
    visited.add(node);
    System.out.print(node + " ");
    for (int neighbor : adj.getOrDefault(node, List.of())) {
        if (!visited.contains(neighbor)) {
            dfs(neighbor, adj, visited);
        }
    }
}

// Iterative
void dfsIterative(int start, Map<Integer, List<Integer>> adj) {
    Set<Integer> visited = new HashSet<>();
    Deque<Integer> stack = new ArrayDeque<>();
    stack.push(start);
    while (!stack.isEmpty()) {
        int node = stack.pop();
        if (visited.contains(node)) continue;
        visited.add(node);
        System.out.print(node + " ");
        for (int neighbor : adj.getOrDefault(node, List.of())) {
            if (!visited.contains(neighbor)) stack.push(neighbor);
        }
    }
}
```

## Example Problem

**Graph:** `1-2, 1-3, 2-4, 3-4, 4-5`
**Goal:** DFS traversal starting from node 1 (recursive, visiting neighbors in ascending order).

## Trace

| Call        | Action                                                                                  | Visited so far |
| ----------- | --------------------------------------------------------------------------------------- | -------------- |
| dfs(1)      | visit 1, look at neighbors 2, 3                                                         | {1}            |
| dfs(2)      | (from 1's first unvisited neighbor) visit 2, look at neighbors 1(visited), 4            | {1,2}          |
| dfs(4)      | (from 2) visit 4, look at neighbors 2(visited), 3, 5                                    | {1,2,4}        |
| dfs(3)      | (from 4) visit 3, look at neighbors 1(visited), 4(visited) — dead end, backtrack        | {1,2,4,3}      |
| dfs(5)      | (back to 4's next neighbor) visit 5, look at neighbors 4(visited) — dead end, backtrack | {1,2,4,3,5}    |
| (back to 1) | neighbor 3 already visited, done                                                        | {1,2,4,3,5}    |

**Result:** traversal order `1, 2, 4, 3, 5` — notice it dove deep through 2→4 before ever reaching 3, unlike BFS which visited 3 right after 1.

## Complexity

- Time: O(V + E)
- Space: O(V) — visited set + recursion/explicit stack (worst case O(V) deep for a skewed graph)

## Key Points / Gotchas

- Use DFS for: cycle detection, topological sort, connected components, path existence, backtracking-style exploration (maze solving, Sudoku), and finding strongly connected components (Tarjan's/Kosaraju's).
- Recursive DFS risks `StackOverflowError` on graphs with very long paths (e.g. a graph with 100,000 nodes in a line) — switch to iterative for large/adversarial inputs.
- Cycle detection differs for directed vs undirected graphs: undirected just needs a visited check (with parent tracking to ignore the trivial back-edge to the immediate parent); directed graphs need a separate "currently in recursion stack" marker to detect back-edges properly.
- Iterative DFS with a stack does **not** produce the same order as recursive DFS in all cases (order of pushing neighbors matters) — don't assume they're interchangeable if exact order matters.

## Related

- See also: bfs, topo-sort, scc
