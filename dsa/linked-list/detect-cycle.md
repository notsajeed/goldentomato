# Detect Cycle (Floyd's Algorithm)

## Intuition

If a linked list has a cycle, a pointer moving through it will loop forever instead of hitting `null`. Rather than using extra memory to track visited nodes (O(n) space), use two pointers moving at different speeds — a slow one (1 step) and a fast one (2 steps). If there's a cycle, the fast pointer will eventually "lap" the slow one and they'll meet inside the loop. If there's no cycle, the fast pointer simply reaches `null` first.

## Definition / How it Works

1. `slow = head`, `fast = head`.
2. Loop while `fast != null && fast.next != null`:
   - `slow = slow.next` (1 step)
   - `fast = fast.next.next` (2 steps)
   - If `slow == fast`, a cycle exists.
3. If the loop exits normally (fast hits null), no cycle.

**Bonus — finding the cycle start:** once `slow == fast`, reset one pointer to `head`, keep the other at the meeting point, then move both 1 step at a time. They meet exactly at the cycle's starting node (this follows from the math of where the meeting point falls relative to the cycle length).

## Code

```java
boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

## Example Problem

**Input:** list `1 -> 2 -> 3 -> 4 -> 5`, where node `5`'s `next` points back to node `2` (cycle).
**Goal:** detect whether a cycle exists.

## Trace

| Step  | slow (1 step) | fast (2 steps) | slow == fast?        |
| ----- | ------------- | -------------- | -------------------- |
| start | 1             | 1              | —                    |
| 1     | 2             | 3              | no                   |
| 2     | 3             | 5              | no                   |
| 3     | 4             | 3 (5→2→3)      | no                   |
| 4     | 5             | 5 (3→4→5)      | yes → cycle detected |

**Result:** `true` — pointers meet at node `5` after 4 iterations, confirming the cycle without any extra memory (a hash-set approach would use O(n) space to track visited nodes instead).

## Complexity

- Time: O(n) — fast pointer traverses at most 2x the cycle length + the tail before entering it
- Space: O(1) — only two pointers, no extra data structure (vs O(n) for a visited-set approach)

## Key Points / Gotchas

- Also called "tortoise and hare" — the name shows up often in problem statements and explanations.
- Must check both `fast != null` **and** `fast.next != null` in the loop condition, or `fast.next.next` throws a NullPointerException on an odd-length non-cyclic list.
- The "find cycle start" trick (reset one pointer to head) is a common follow-up — know the two-phase approach, not just detection.
- Same two-pointer speed trick generalizes to "find the middle of a linked list" (slow ends at middle when fast hits the end) and "find nth node from the end".

## Related

- See also: singly-linked-list, reverse-linked-list
