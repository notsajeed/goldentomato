# Stack

## Intuition

A stack is LIFO — Last In, First Out. Think of a stack of plates: you can only add or remove from the top. This restriction is exactly what makes it useful: it naturally models "undo" history, function call frames, and any problem where you need to process the most recently seen item first (matching brackets, backtracking, DFS).

## Definition / How it Works

Two core operations, both O(1):

- **push(x)**: add `x` to the top.
- **pop()**: remove and return the top element.
- **peek()/top()**: look at the top element without removing it.
- **isEmpty()**: check if the stack has no elements.

Can be implemented with an array (dynamic array, push/pop at the end — O(1) amortized) or a linked list (push/pop at the head — O(1) always, no resizing).

## Code

```java
Deque<Integer> stack = new ArrayDeque<>(); // Java's recommended stack impl
stack.push(10);
stack.push(20);
stack.push(30);
int top = stack.peek();  // 30
int popped = stack.pop(); // 30, stack now [10, 20]
```

## Example Problem

**Input:** operations `push(5)`, `push(8)`, `push(3)`, `pop()`, `peek()`
**Goal:** trace the stack state after each operation.

## Trace

| Operation | Stack (top on right) | Returned value |
| --------- | -------------------- | -------------- |
| push(5)   | [5]                  | —              |
| push(8)   | [5, 8]               | —              |
| push(3)   | [5, 8, 3]            | —              |
| pop()     | [5, 8]               | 3              |
| peek()    | [5, 8]               | 8              |

**Result:** final stack `[5, 8]`, last `pop()` returned `3` (most recently pushed remaining element).

## Complexity

- push / pop / peek / isEmpty: O(1)
- Space: O(n)

## Key Points / Gotchas

- In Java, avoid the legacy `Stack` class (synchronized, slower) — use `ArrayDeque` instead, it's the recommended stack/queue implementation.
- Classic uses: balanced parentheses/bracket matching, expression evaluation (infix→postfix, postfix evaluation), undo functionality, DFS (iterative, using an explicit stack instead of recursion), browser back button history.
- Function call stack in any language is literally a stack — this is _why_ deep recursion causes a "stack overflow".
- Always check `isEmpty()` before `pop()`/`peek()` — popping an empty stack is a common runtime-crash bug.

## Related

- See also: queue-basics, valid-parentheses, monotonic-stack
