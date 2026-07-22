# Valid Parentheses

## Intuition

To check if brackets are balanced and correctly nested, you need to remember which opening bracket you're currently "inside of" so you can match it against the next closing bracket. A stack does exactly this: push every opening bracket, and when a closing bracket appears, it must match whatever's on top of the stack (the most recently opened, still-unclosed bracket).

## Definition / How it Works

1. Scan the string left to right.
2. If the character is an opening bracket (`(`, `{`, `[`), push it onto the stack.
3. If it's a closing bracket (`)`, `}`, `]`):
   - If the stack is empty, there's nothing to match → invalid.
   - Pop the stack and check it matches the corresponding opening bracket → if not, invalid.
4. After scanning, the string is valid only if the stack is empty (every opener was matched).

## Code

```java
boolean isValid(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    Map<Character, Character> pairs = Map.of(')', '(', ']', '[', '}', '{');
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else {
            if (stack.isEmpty() || stack.pop() != pairs.get(c)) return false;
        }
    }
    return stack.isEmpty();
}
```

## Example Problem

**Input:** `s = "{[()]}"`
**Goal:** determine if brackets are validly matched and nested.

## Trace

| Char | Action                           | Stack after |
| ---- | -------------------------------- | ----------- |
| `{`  | push                             | [{]         |
| `[`  | push                             | [{, []      |
| `(`  | push                             | [{, [, (]   |
| `)`  | pop, check `(` matches `)` → yes | [{, []      |
| `]`  | pop, check `[` matches `]` → yes | [{]         |
| `}`  | pop, check `{` matches `}` → yes | []          |

**Result:** stack empty at end → `true` (valid). Compare with `s = "([)]"`: at `)`, stack top is `[`, which doesn't match `)` → `false` immediately, even though bracket _counts_ are balanced — order matters, not just counts.

## Complexity

- Time: O(n) — single pass
- Space: O(n) worst case (all opening brackets, e.g. `"((((("`)

## Key Points / Gotchas

- Counting brackets (equal number of `(` and `)`) is **not** sufficient — `"([)]"` has equal counts but is invalid due to incorrect nesting order. The stack captures order, not just count.
- Early exit on empty-stack-pop or mismatch avoids unnecessary work — check this before continuing the scan.
- A non-empty stack at the end means unclosed openers (e.g. `"(("`) — must explicitly check `stack.isEmpty()` at the end, not just during the scan.
- Extend to other pairing problems: HTML/XML tag matching, expression parenthesization checks — same core pattern.

## Related

- See also: stack-basics, monotonic-stack
