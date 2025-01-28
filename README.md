# Obsidian Property Remove

This script allows you to remove specific properties from all Markdown files in an Obsidian vault. It's useful for cleaning up unwanted metadata or other properties that may have been added to your notes.

## How It Works

The script scans all `.md` files in your Obsidian vault, identifies the lines containing the property you wish to remove, and then rewrites the files without those lines.

## Requirements

- Python 3.x
- Access to your Obsidian vault path

## Setup

1. Clone the repository or download the script.
2. Replace the `vault_path` with the path to your Obsidian vault on your local machine.
3. Specify the `property_to_remove` with the property or metadata you want to remove (e.g., `name-property:`).

## Example Usage

```python
import os

vault_path = os.path.expanduser("~/Projects/Obsidian-vault")

property_to_remove = "notes:"


for root, _, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"): 
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()  # Read all lines from the file
            # Filter out lines containing the property to remove
            new_lines = [line for line in lines if property_to_remove not in line]
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)  # Write the updated lines back to the file

print("Property(ies) removed successfully!")
