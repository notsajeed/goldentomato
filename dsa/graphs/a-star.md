# A\* Search

## Intuition

Dijkstra's finds shortest paths by exploring outward in all directions equally, with no sense of "which direction is promising." A\* adds a **heuristic** — an estimate of remaining distance to the goal — to guide the search toward the target faster, while still guaranteeing the optimal path (as long as the heuristic never overestimates the true remaining distance). It's Dijkstra's plus a compass pointing roughly toward the goal.

## Definition / How it Works

For each node, A\* tracks:

- `g(n)` = actual cost from start to `n` (same as Dijkstra's `dist`)
- `h(n)` = heuristic estimate of cost from `n` to the goal (problem-specific — e.g. straight-line/Euclidean distance for grid pathfinding)
- `f(n) = g(n) + h(n)` — estimated total cost of a path through `n`

Algorithm: same structure as Dijkstra's (min-heap, relax neighbors), but the heap is ordered by `f(n)` instead of `g(n)` alone. This means nodes that look promising (low estimated total cost) get explored first, pruning away directions that are unlikely to lead to a shorter path.

**Admissibility requirement**: for A* to guarantee the optimal path, `h(n)` must never overestimate the true remaining cost. If it overestimates, A* may return a suboptimal path (though it'll typically run faster).

## Code

```java
// Grid pathfinding, h = Manhattan distance to goal
int aStar(int[][] grid, int[] start, int[] goal) {
    int rows = grid.length, cols = grid[0].length;
    int[][] gScore = new int[rows][cols];
    for (int[] row : gScore) Arrays.fill(row, Integer.MAX_VALUE);
    gScore[start[0]][start[1]] = 0;

    PriorityQueue<int[]> openSet = new PriorityQueue<>((a, b) -> a[0] - b[0]); // [f, row, col]
    openSet.offer(new int[]{heuristic(start, goal), start[0], start[1]});

    int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!openSet.isEmpty()) {
        int[] curr = openSet.poll();
        int r = curr[1], c = curr[2];
        if (r == goal[0] && c == goal[1]) return gScore[r][c];

        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == 1) continue; // wall
            int tentativeG = gScore[r][c] + 1;
            if (tentativeG < gScore[nr][nc]) {
                gScore[nr][nc] = tentativeG;
                int f = tentativeG + heuristic(new int[]{nr, nc}, goal);
                openSet.offer(new int[]{f, nr, nc});
            }
        }
    }
    return -1; // no path found
}

int heuristic(int[] a, int[] b) {
    return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]); // Manhattan distance
}
```

## Example Problem

**Grid (0=open, 1=wall):** 3x3 grid, start=(0,0), goal=(2,2), wall at (1,1).
**Goal:** find shortest path length using A\* with Manhattan distance heuristic.

## Trace

`h(node) = |row - 2| + |col - 2|`. Start: `g=0, h=4, f=4`.

| Pop (f, node) | g so far | Expand neighbors                        | New f values | Notes                               |
| ------------- | -------- | --------------------------------------- | ------------ | ----------------------------------- |
| (4, (0,0))    | 0        | (0,1): g=1,h=3,f=4; (1,0): g=1,h=3,f=4  | push both    | wall at (1,1) not adjacent yet      |
| (4, (0,1))    | 1        | (0,2): g=2,h=2,f=4; (1,1) is wall, skip | push (0,2)   | heuristic keeps guiding toward goal |
| (4, (1,0))    | 1        | (2,0): g=2,h=2,f=4; (1,1) wall, skip    | push (2,0)   |                                     |
| (4, (0,2))    | 2        | (1,2): g=3,h=1,f=4                      | push (1,2)   | getting close                       |
| (4, (2,0))    | 2        | (2,1): g=3,h=1,f=4                      | push (2,1)   |                                     |
| (4, (1,2))    | 3        | (2,2): g=4,h=0,f=4                      | push goal    |                                     |
| (4, (2,2))    | 4        | **goal reached**                        | —            | return g=4                          |

**Result:** shortest path length = **4** steps (e.g. (0,0)→(0,1)→(0,2)→(1,2)→(2,2)), found while only exploring nodes the heuristic considered promising — Dijkstra's would have explored more nodes uniformly in all directions before confirming the same answer.

## Complexity

- Time: O(E) in the best case with a very accurate heuristic, up to O((V+E) log V) worst case (same as Dijkstra's if the heuristic is uninformative, e.g. `h(n) = 0` always — which literally reduces A\* to Dijkstra's)
- Space: O(V) for the open set and score tracking

## Key Points / Gotchas

- If `h(n) = 0` for all nodes, A\* becomes exactly Dijkstra's — a good way to remember the relationship between the two.
- The heuristic must be **admissible** (never overestimates) for optimality; Manhattan distance works for grids with 4-directional movement, Euclidean distance for any-angle movement — using Manhattan distance with diagonal movement allowed would overestimate and break optimality.
- A heuristic that's admissible **and consistent** (satisfies a triangle-inequality-like property) also avoids needing to re-open already-finalized nodes, simplifying implementation.
- Extremely common in pathfinding for games and robotics — the heuristic is what makes it dramatically faster than Dijkstra's in practice on large maps, despite the same worst-case complexity.

## Related

- See also: dijkstra, bfs
