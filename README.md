# Obsidian Property Remove

This script allows you to remove specific properties from all Markdown files in an Obsidian vault. It's useful for cleaning up unwanted metadata or other properties that may have been added to your notes.

## How It Works

The script scans all `.md` files in your Obsidian vault, identifies the lines containing the property you wish to remove, and then rewrites the files without those lines.


## Requirements

- Python 3.x
- Access to your Obsidian vault path

## Setup

1. Clone the repository or download the script.

``` bash
   git clone https://github.com/pedrorcruzz/obsidian-property-remove.git
```
2. Replace the `vault_path` with the path to your Obsidian vault on your local machine.
3. Specify the `property_to_remove` with the property or metadata you want to remove (e.g., `name-property:`).
4. run code

```python
    python3 main.py
```

## Example Usage


 Important: The property to remove must follow the format property-name: and must include the colon (:) for it to be identified correctly.

```python
vault_path = os.path.expanduser("~/Projects/Obsidian-vault")

property_to_remove = "notes:"
```
