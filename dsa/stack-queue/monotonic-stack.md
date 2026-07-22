# Monotonic Stack

## Intuition

A monotonic stack keeps its elements always increasing or always decreasing from bottom to top. It's the go-to pattern for "next greater/smaller element" style problems, because it lets you find, for each element, the nearest element to its left or right that's bigger/smaller — in a single O(n) pass instead of O(n²) brute force comparison of every pair.

## Definition / How it Works

For "next greater element" (scanning left to right, using a **decreasing** stack of indices):

1. For each new element, while the stack isn't empty and the current element is greater than the element at the stack's top index, pop the stack — the popped element's "next greater" is the current element.
2. Push the current index onto the stack.
3. Any indices left on the stack at the end have no next greater element (typically marked -1 or 0).

The key insight: once a bigger element appears, all smaller elements below it in the stack can never find _anything_ better than this one going forward for "next greater" — so they get resolved and popped immediately, keeping every element pushed and popped at most once.

## Code

```java
int[] nextGreaterElement(int[] arr) {
    int n = arr.length;
    int[] result = new int[n];
    Arrays.fill(result, -1);
    Deque<Integer> stack = new ArrayDeque<>(); // stores indices, decreasing values
    for (int i = 0; i < n; i++) {
        while (!stack.isEmpty() && arr[i] > arr[stack.peek()]) {
            int idx = stack.pop();
            result[idx] = arr[i];
        }
        stack.push(i);
    }
    return result;
}
```

## Example Problem

**Input:** `arr = [2, 1, 2, 4, 3]`
**Goal:** find the next greater element for each index.

## Trace

| i   | arr[i] | stack before (indices) | pops (arr[i] > arr[top]?)                                              | result updates           | stack after                           |
| --- | ------ | ---------------------- | ---------------------------------------------------------------------- | ------------------------ | ------------------------------------- |
| 0   | 2      | []                     | —                                                                      | —                        | [0]                                   |
| 1   | 1      | [0]                    | 1 > 2? no                                                              | —                        | [0, 1]                                |
| 2   | 2      | [0, 1]                 | 2 > 1? yes, pop 1                                                      | result[1] = 2            | [0] (2>2? no, stop) → push 2 → [0, 2] |
| 3   | 4      | [0, 2]                 | 4 > 2? yes, pop 2 → result[2]=4; 4 > 2(idx0)? yes, pop 0 → result[0]=4 | result[2]=4, result[0]=4 | [3]                                   |
| 4   | 3      | [3]                    | 3 > 4? no                                                              | —                        | [3, 4]                                |

**Result:** `result = [4, 2, 4, -1, -1]` — index 3 (value 4) and index 4 (value 3) have no next greater element, correctly left as -1.

## Complexity

- Time: O(n) — each index is pushed once and popped at most once, despite the nested-looking while loop
- Space: O(n) — stack in the worst case (strictly decreasing input never pops early)

## Key Points / Gotchas

- The O(n) claim despite the `while` loop inside a `for` loop is the classic "amortized analysis" interview follow-up — total pops across the entire run is bounded by total pushes (n), so it's not O(n²).
- Store **indices** on the stack, not values — you need the index to write into the `result` array, and comparing `arr[stack.peek()]` still gives you the value when needed.
- Variants: next smaller element (flip the comparison), previous greater/smaller (scan right to left, or track differently), "largest rectangle in histogram" (a harder application of the same pattern).
- Distinguish from a plain stack: "monotonic" just describes an _invariant_ you maintain via conditional pops before every push — same underlying stack structure.

## Related

- See also: stack-basics, valid-parentheses
