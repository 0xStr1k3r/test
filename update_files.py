#!/usr/bin/env python3
import os
import json
import hashlib
from datetime import datetime

def get_file_info(filepath):
    """Get file information for a markdown file."""
    stat = os.stat(filepath)
    return {
        "name": os.path.basename(filepath),
        "path": filepath.replace('./', ''),
        "size": stat.st_size,
        "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "raw_url": filepath.replace('./', '')
    }

def find_md_files(directory='.'):
    """Find all .md files in the directory recursively."""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                md_files.append(filepath)
    return sorted(md_files)

def update_files_json():
    """Update files.json with current .md files."""
    md_files = find_md_files()
    files_data = [get_file_info(f) for f in md_files]

    with open('files.json', 'w') as f:
        json.dump(files_data, f, indent=2)

    print(f"Updated files.json with {len(files_data)} markdown files")

if __name__ == "__main__":
    update_files_json()