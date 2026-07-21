# Singly Linked List

## Intuition

An array needs contiguous memory and costly insert/delete in the middle (O(n) shifting). A linked list trades random access (no O(1) indexing) for O(1) insertion/deletion at a known position, by chaining nodes together with pointers instead of storing elements contiguously.

## Definition / How it Works

Each node holds a `value` and a `next` pointer to the following node (or `null` if it's the last). The list is accessed via a `head` reference. Traversal means following `next` pointers one at a time — there's no way to jump to index `i` directly.

Core operations:

- **Insert at head**: new node's `next = head`, then `head = new node`. O(1).
- **Insert at tail**: traverse to the last node, set its `next` to the new node. O(n) without a tail pointer, O(1) with one.
- **Delete a node**: find the node before the target, re-point its `next` to skip over the target. O(n) to find, O(1) to unlink.
- **Traverse**: start at `head`, follow `next` until `null`.

## Code

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

// Insert at head
ListNode insertHead(ListNode head, int val) {
    ListNode newNode = new ListNode(val);
    newNode.next = head;
    return newNode; // new head
}

// Traverse and print
void printList(ListNode head) {
    while (head != null) {
        System.out.print(head.val + " -> ");
        head = head.next;
    }
    System.out.println("null");
}
```

## Example Problem

**Input:** build a list by inserting 3, then 2, then 1 at the head.
**Goal:** show resulting structure and traversal order.

## Trace

| Action                  | List after action |
| ----------------------- | ----------------- |
| insertHead(null, 3)     | 3 → null          |
| insertHead(3→null, 2)   | 2 → 3 → null      |
| insertHead(2→3→null, 1) | 1 → 2 → 3 → null  |

**Traversal output:** `1 -> 2 -> 3 -> null`

**Result:** each `insertHead` is O(1) regardless of list size — contrast with an array where inserting at index 0 requires shifting every existing element.

## Complexity

- Access/Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(1) with tail pointer, O(n) without
- Delete: O(n) to find + O(1) to unlink
- Space: O(n) — plus O(1) extra per node for the pointer (overhead array doesn't have)

## Key Points / Gotchas

- Always handle `head == null` (empty list) and single-node list as edge cases — most linked list bugs live in these boundaries.
- Use a **dummy/sentinel head** node in insert/delete problems to avoid special-casing "operation on the actual head" — a very common interview trick.
- Doubly linked list adds a `prev` pointer, trading extra memory for O(1) backward traversal and O(1) deletion given only a node reference (no need to find the predecessor).
- Losing the `next` pointer before saving it (e.g. during reversal) is the single most common linked-list bug — always save `next` before overwriting it.

## Related

- See also: reverse-linked-list, detect-cycle, merge-two-lists
