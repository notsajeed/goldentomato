# Queue

## Intuition

A queue is FIFO — First In, First Out, like a real-world line: whoever arrives first gets served first. This ordering is essential for anything that processes items in the order they arrived — task scheduling, BFS traversal, request handling.

## Definition / How it Works

Two ends: **rear** (where elements are added) and **front** (where elements are removed).

- **enqueue(x)**: add `x` to the rear.
- **dequeue()**: remove and return the element at the front.
- **peek()/front()**: look at the front element without removing it.

A naive array-based queue has an O(n) dequeue (shifting all elements left). A **circular buffer** or a doubly-linked list avoids this, giving O(1) for both operations.

## Code

```java
Deque<Integer> queue = new ArrayDeque<>(); // works as a queue too
queue.offer(10); // enqueue
queue.offer(20);
queue.offer(30);
int front = queue.peek();  // 10
int removed = queue.poll(); // 10, queue now [20, 30]
```

## Example Problem

**Input:** operations `enqueue(5)`, `enqueue(8)`, `enqueue(3)`, `dequeue()`, `peek()`
**Goal:** trace the queue state after each operation.

## Trace

| Operation  | Queue (front → rear) | Returned value |
| ---------- | -------------------- | -------------- |
| enqueue(5) | [5]                  | —              |
| enqueue(8) | [5, 8]               | —              |
| enqueue(3) | [5, 8, 3]            | —              |
| dequeue()  | [8, 3]               | 5              |
| peek()     | [8, 3]               | 8              |

**Result:** final queue `[8, 3]`, `dequeue()` returned `5` (the earliest-added remaining element) — opposite order from a stack's `pop()` on the same input.

## Complexity

- enqueue / dequeue / peek: O(1) with circular buffer or linked list; naive array dequeue is O(n)
- Space: O(n)

## Key Points / Gotchas

- Classic uses: BFS traversal (level-order processing), task/job scheduling, print queues, rate limiting (sliding window counters), producer-consumer buffering.
- **Circular queue**: wraps `rear` and `front` indices back to 0 using modulo, so a fixed-size array can be reused without shifting — avoids the O(n) naive-array dequeue cost.
- **Deque** (double-ended queue) generalizes both stack and queue — insertion/removal at both ends in O(1). Used in sliding window maximum problems.
- **Priority queue** is a different structure entirely (usually a heap) — elements come out by priority, not insertion order; don't confuse the two.

## Related

- See also: stack-basics, bfs
