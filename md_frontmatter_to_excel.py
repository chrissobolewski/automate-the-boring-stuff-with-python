#!/usr/bin/env python3
import os
import sys
import argparse
import json
import frontmatter
import pandas as pd

def normalize_value(v):
    if v is None:
        return ""
    if isinstance(v, (str, int, float, bool)):
        return v
    if isinstance(v, (list, tuple)):
        # If list is simple (scalars), join; else JSON
        if all(isinstance(x, (str, int, float, bool, type(None))) for x in v):
            return ", ".join("" if x is None else str(x) for x in v)
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False)
    return str(v)

def collect_markdown_files(path, recursive=True):
    files = []
    if os.path.isfile(path) and path.lower().endswith(".md"):
        return [os.path.abspath(path)]
    if os.path.isdir(path):
        if recursive:
            for root, _, filenames in os.walk(path):
                for name in filenames:
                    if name.lower().endswith(".md"):
                        files.append(os.path.join(root, name))
        else:
            for name in os.listdir(path):
                full = os.path.join(path, name)
                if os.path.isfile(full) and name.lower().endswith(".md"):
                    files.append(full)
    return [os.path.abspath(f) for f in files]

def main():
    parser = argparse.ArgumentParser(description="Extract YAML front matter from Markdown files to Excel.")
    parser.add_argument("input_path", help="Path to a Markdown file or a directory containing .md files")
    parser.add_argument("output_excel", help="Path to the output .xlsx file (e.g., output.xlsx)")
    parser.add_argument("--no-recursive", action="store_true", help="Do not search subfolders when input is a directory")
    args = parser.parse_args()

    md_files = collect_markdown_files(args.input_path, recursive=not args.no_recursive)
    if not md_files:
        print("No Markdown files found.", file=sys.stderr)
        sys.exit(1)

    records = []
    for fpath in md_files:
        try:
            post = frontmatter.load(fpath)
            meta = post.metadata if isinstance(post.metadata, dict) else {}
        except Exception as e:
            # If a file can't be parsed, still include filename and note the error
            meta = {"_parse_error": str(e)}

        row = {"filename": os.path.basename(fpath)}
        for k, v in meta.items():
            row[str(k)] = normalize_value(v)
        records.append(row)

    # Build DataFrame with union of all keys, filename first
    all_keys = set()
    for r in records:
        all_keys.update(r.keys())
    cols = ["filename"] + sorted(k for k in all_keys if k != "filename")
    df = pd.DataFrame(records)
    df = df.reindex(columns=cols)

    # Write Excel
    out_path = os.path.abspath(args.output_excel)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    df.to_excel(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path}")

if __name__ == "__main__":
    main()