# Longest Common Subsequence (LCS)

## Intuition

Given two strings, find the length of the longest sequence of characters that appears in both, in the same relative order but **not necessarily contiguous** (a subsequence, not a substring). For example, "ace" is a subsequence of "abcde". This is the foundation for diff tools (git diff, version control), DNA sequence comparison, and spell-check/autocorrect distance metrics.

## Definition / How it Works

Define `dp[i][j]` = length of LCS between the first `i` characters of string A and the first `j` characters of string B.

- If `A[i-1] == B[j-1]` (characters match): this character extends the LCS found without it → `dp[i][j] = dp[i-1][j-1] + 1`.
- If they don't match: the LCS is the best of either ignoring the current character of A, or ignoring the current character of B → `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Base case: `dp[0][j] = dp[i][0] = 0` (LCS with an empty string is always 0).

## Code

```java
int lcs(String a, String b) {
    int n = a.length(), m = b.length();
    int[][] dp = new int[n + 1][m + 1];

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a.charAt(i - 1) == b.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[n][m];
}
```

## Example Problem

**Input:** `a = "ABCBDAB"`, `b = "BDCAB"`
**Goal:** length of longest common subsequence.

## Trace

Simplified with shorter strings for clarity — `a = "ABC"`, `b = "AC"`:

| dp[i][j] | ""  | A   | C   |
| -------- | --- | --- | --- |
| ""       | 0   | 0   | 0   |
| A        | 0   | 1   | 1   |
| B        | 0   | 1   | 1   |
| C        | 0   | 1   | 2   |

**Key cells:**

- `dp[1][1]` (A vs A): match → `dp[0][0]+1 = 1`
- `dp[2][1]` (B vs A): no match → `max(dp[1][1], dp[2][0]) = max(1,0) = 1`
- `dp[3][2]` (C vs C): match → `dp[2][1]+1 = 1+1 = 2`

**Result:** `dp[3][2] = 2` — LCS is "AC" (both characters appear in order in both strings), length 2.

For the original longer example `"ABCBDAB"` vs `"BDCAB"`, the same table-building process yields LCS length **4** (one valid LCS: "BCAB" or "BDAB").

## Complexity

- Time: O(n × m)
- Space: O(n × m), reducible to O(min(n,m)) using a rolling 1D array (only the previous row is ever needed)

## Key Points / Gotchas

- Don't confuse **subsequence** (order preserved, gaps allowed) with **substring** (must be contiguous) — "longest common substring" is a different, related problem solved similarly but resets to 0 on a mismatch instead of taking the max.
- To reconstruct the actual LCS string (not just its length), backtrack from `dp[n][m]`: if characters matched, move diagonally and record the char; otherwise move toward whichever of `dp[i-1][j]`/`dp[i][j-1]` was larger.
- Base for many related problems: edit distance (Levenshtein), longest palindromic subsequence (LCS of a string with its reverse), shortest common supersequence.
- Real-world use: `diff` and `git diff` compute something conceptually related to LCS to identify unchanged lines between file versions.

## Related

- See also: knapsack-01
