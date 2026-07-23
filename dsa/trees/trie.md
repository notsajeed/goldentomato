# Trie (Prefix Tree)

## Intuition

Storing a set of strings in a hash set answers "does this exact word exist?" in O(1), but can't efficiently answer "what words start with this prefix?" without scanning everything. A trie stores strings character by character down a tree, so that all words sharing a prefix share the same path from the root — prefix queries become a single O(L) walk (L = prefix length) instead of scanning every stored word.

## Definition / How it Works

Each trie node holds:

- A map/array of children, one per possible next character (e.g. 26 slots for lowercase English letters).
- A boolean flag `isEndOfWord` marking whether a complete word ends at this node.

- **Insert(word)**: walk from the root, creating child nodes for characters that don't exist yet, and mark `isEndOfWord = true` at the final character's node.
- **Search(word)**: walk the path for each character; if any character's child is missing, the word doesn't exist. If the full path exists, return `isEndOfWord` at the last node (must be a complete word, not just a prefix of something else).
- **StartsWith(prefix)**: same walk as search, but return `true` as soon as the full path exists — don't check `isEndOfWord`.

## Code

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord = false;
}

class Trie {
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) node.children[idx] = new TrieNode();
            node = node.children[idx];
        }
        node.isEndOfWord = true;
    }

    boolean search(String word) {
        TrieNode node = find(word);
        return node != null && node.isEndOfWord;
    }

    boolean startsWith(String prefix) {
        return find(prefix) != null;
    }

    private TrieNode find(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return null;
            node = node.children[idx];
        }
        return node;
    }
}
```

## Example Problem

**Input:** insert `"cat"`, `"car"`, `"dog"`. Then check `search("car")`, `search("ca")`, `startsWith("ca")`.
**Goal:** show how shared prefixes ("ca" in cat/car) share trie nodes.

## Trace

**After inserting "cat", "car", "dog":**

```
root
├── c → a → t (isEndOfWord=true)
│         └→ r (isEndOfWord=true)
└── d → o → g (isEndOfWord=true)
```

Note: `c → a` is a single shared path for both "cat" and "car" — only 4 unique nodes needed for "cat"+"car" combined, not 6.

| Query            | Path walked | Ends at valid node? | isEndOfWord?                                      | Result  |
| ---------------- | ----------- | ------------------- | ------------------------------------------------- | ------- |
| search("car")    | root→c→a→r  | yes                 | true                                              | `true`  |
| search("ca")     | root→c→a    | yes                 | **false** (only a prefix, not inserted as a word) | `false` |
| startsWith("ca") | root→c→a    | yes                 | (not checked)                                     | `true`  |

**Result:** `search("ca")` is `false` but `startsWith("ca")` is `true` — the key distinction between the two operations.

## Complexity

- Insert / Search / StartsWith: O(L) where L = length of the word/prefix — independent of how many words are stored
- Space: O(ALPHABET_SIZE × N × L) worst case (N words of length L, no shared prefixes) — but shared prefixes reduce this significantly in practice

## Key Points / Gotchas

- The core value proposition is **prefix operations** — autocomplete, spell-check, IP routing (longest prefix match) all use tries because "all words starting with X" is a single subtree, not a scan.
- `search()` must check `isEndOfWord`, `startsWith()` must not — mixing these up is the most common trie bug.
- Fixed-size array (26 children) is fast but wastes memory for sparse alphabets — a `HashMap<Character, TrieNode>` trades some speed for memory efficiency when the character set is large (Unicode) or usage is sparse.
- Common interview extension: "word search II" / "longest word with all prefixes present" — both lean on the prefix-sharing property directly.

## Related

- See also: bst
