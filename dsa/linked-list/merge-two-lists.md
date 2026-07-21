# Merge Two Sorted Lists

## Intuition

Given two already-sorted linked lists, produce one sorted list containing all their nodes — without extra sorting. Since both inputs are sorted, at any point the smallest remaining element is at the front of one of the two lists. Repeatedly pick the smaller front node and advance that list, exactly like the merge step in merge sort but on linked structures instead of arrays.

## Definition / How it Works

Use a **dummy head** node to simplify edge cases (no need to special-case "what's the very first node of the result"). Maintain a `tail` pointer to the last node appended so far.

1. While both lists have nodes left: compare their front values, attach the smaller one to `tail.next`, advance that list's pointer and `tail`.
2. When one list runs out, attach the remainder of the other list directly (it's already sorted, no need to walk it node by node).
3. Return `dummy.next` (skipping the placeholder).

## Code

```java
ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(-1);
    ListNode tail = dummy;
    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) {
            tail.next = l1;
            l1 = l1.next;
        } else {
            tail.next = l2;
            l2 = l2.next;
        }
        tail = tail.next;
    }
    tail.next = (l1 != null) ? l1 : l2; // attach remainder
    return dummy.next;
}
```

## Example Problem

**Input:** `l1 = 1 -> 3 -> 5`, `l2 = 2 -> 4 -> 6`
**Goal:** merge into one sorted list.

## Trace

| Step | l1   | l2  | compare      | attach                        | tail now |
| ---- | ---- | --- | ------------ | ----------------------------- | -------- |
| 1    | 1    | 2   | 1 ≤ 2        | attach 1, l1→3                | 1        |
| 2    | 3    | 2   | 3 > 2        | attach 2, l2→4                | 2        |
| 3    | 3    | 4   | 3 ≤ 4        | attach 3, l1→5                | 3        |
| 4    | 5    | 4   | 5 > 4        | attach 4, l2→6                | 4        |
| 5    | 5    | 6   | 5 ≤ 6        | attach 5, l1→null             | 5        |
| 6    | null | 6   | l1 exhausted | attach remainder (6) directly | 6        |

**Result:** `1 -> 2 -> 3 -> 4 -> 5 -> 6`, built in one pass without any extra sorting step.

## Complexity

- Time: O(n + m) where n, m are the lengths of the two lists — each node visited once
- Space: O(1) extra — reuses existing nodes, only the dummy node is new (O(n+m) if a recursive version is used, due to call stack)

## Key Points / Gotchas

- The dummy head trick eliminates a whole class of "is this the first node?" bugs — use it any time you're building a list from scratch.
- Don't forget the final `tail.next = remainder` step — a common mistake is looping until _both_ lists are empty (wasteful) instead of attaching the leftover chunk directly.
- Recursive version is more concise (`if l1.val <= l2.val: l1.next = merge(l1.next, l2); return l1` etc.) but trades O(1) space for O(n+m) call stack.
- Generalizes to "merge k sorted lists" using a min-heap of size k instead of comparing just two fronts — same core idea, different data structure to find the minimum.

## Related

- See also: singly-linked-list, merge (sort)
