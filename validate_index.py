#!/usr/bin/env python3
"""
validate_index.py

Checks that every "path" referenced in index.json actually exists as a file
in the repo, and flags any .md files that exist but aren't referenced in
index.json (orphan files the app will never show).

Usage:
    python validate_index.py                # run from repo root
    python validate_index.py /path/to/repo   # or pass repo root explicitly
"""

import json
import os
import sys


def load_index(repo_root):
    index_path = os.path.join(repo_root, "index.json")
    if not os.path.isfile(index_path):
        print(f"ERROR: index.json not found at {index_path}")
        sys.exit(1)
    with open(index_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_paths(index_data):
    """Walk subjects -> categories -> topics and collect (id, path) pairs."""
    entries = []
    for subject in index_data.get("subjects", []):
        for category in subject.get("categories", []):
            for topic in category.get("topics", []):
                entries.append({
                    "subject": subject.get("id"),
                    "category": category.get("id"),
                    "topic_id": topic.get("id"),
                    "topic_name": topic.get("name"),
                    "path": topic.get("path"),
                })
    return entries


def find_all_md_files(repo_root):
    """Find every .md file in the repo (relative paths, forward slashes)."""
    md_files = set()
    for dirpath, _, filenames in os.walk(repo_root):
        for fname in filenames:
            if fname.endswith(".md"):
                full = os.path.join(dirpath, fname)
                rel = os.path.relpath(full, repo_root).replace(os.sep, "/")
                md_files.add(rel)
    return md_files


def validate(repo_root):
    index_data = load_index(repo_root)
    entries = extract_paths(index_data)

    missing = []
    matched_paths = set()

    for e in entries:
        path = e["path"]
        if not path:
            missing.append({**e, "reason": "no 'path' field in index.json"})
            continue
        full_path = os.path.join(repo_root, path)
        if os.path.isfile(full_path):
            matched_paths.add(path)
        else:
            missing.append({**e, "reason": "file not found on disk"})

    all_md = find_all_md_files(repo_root)
    orphans = sorted(all_md - matched_paths)

    print("=" * 60)
    print(f"Checked {len(entries)} entries in index.json")
    print("=" * 60)

    if missing:
        print(f"\n MISSING / BROKEN ({len(missing)}):")
        for m in missing:
            print(f"  - [{m['subject']}/{m['category']}] "
                  f"id='{m['topic_id']}' name='{m['topic_name']}' "
                  f"path='{m['path']}' -> {m['reason']}")
    else:
        print("\n All index.json paths resolve to real files.")

    if orphans:
        print(f"\n ORPHAN FILES not referenced in index.json ({len(orphans)}):")
        for o in orphans:
            print(f"  - {o}")
    else:
        print("\n No orphan .md files.")

    print("\n" + "=" * 60)
    if missing:
        sys.exit(1)  # non-zero exit so this can be used in CI / pre-push hook
    sys.exit(0)


if __name__ == "__main__":
    repo_root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    validate(repo_root)