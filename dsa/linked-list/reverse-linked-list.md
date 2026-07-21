# Reverse Linked List

## Intuition

Reversing means flipping every node's `next` pointer to point backward instead of forward. Since each node only knows its `next` (not its previous), you need to track the previous node manually as you walk forward, or you'll lose the ability to go back.

## Definition / How it Works

Iterative approach uses three pointers: `prev` (starts null), `curr` (starts at head), and a temporary `next` to save the forward link before overwriting it.

At each step:

1. Save `next = curr.next` (don't lose the rest of the list).
2. Reverse the link: `curr.next = prev`.
3. Advance both: `prev = curr`, `curr = next`.
4. When `curr` becomes null, `prev` is the new head.

## Code

```java
ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;
    while (curr != null) {
        ListNode next = curr.next; // save before overwriting
        curr.next = prev;          // reverse the pointer
        prev = curr;                // advance prev
        curr = next;                 // advance curr
    }
    return prev; // new head
}
```

## Example Problem

**Input:** `1 -> 2 -> 3 -> null`
**Goal:** reverse to `3 -> 2 -> 1 -> null`.

## Trace

| Step            | prev | curr | next (saved) | curr.next set to | list state (conceptual)  |
| --------------- | ---- | ---- | ------------ | ---------------- | ------------------------ |
| start           | null | 1    | —            | —                | 1→2→3→null               |
| 1               | null | 1    | 2            | 1.next = null    | null←1 2→3→null          |
| 2               | 1    | 2    | 3            | 2.next = 1       | null←1←2 3→null          |
| 3               | 2    | 3    | null         | 3.next = 2       | null←1←2←3               |
| end (curr=null) | 3    | null | —            | —                | loop ends, return prev=3 |

**Result:** `3 -> 2 -> 1 -> null`, done in one pass, O(1) extra space (just the three pointers).

## Complexity

- Time: O(n) — visits each node once
- Space: O(1) iterative, O(n) recursive (call stack depth = list length)

## Key Points / Gotchas

- The order of the three lines inside the loop matters — save `next` _before_ reassigning `curr.next`, or the rest of the list becomes unreachable.
- Recursive version exists too: `reverseList(head.next)` first, then fix pointers on the way back up — elegant but O(n) space vs iterative O(1).
- Common follow-up: **reverse only a sublist** between positions `left` and `right` — same core mechanic but bounded to a segment, with careful reconnection to the untouched parts.
- Also common: reverse in groups of `k` (e.g. LeetCode "Reverse Nodes in k-Group") — repeatedly applies this exact three-pointer reversal to each group.

## Related

- See also: singly-linked-list, detect-cycle
