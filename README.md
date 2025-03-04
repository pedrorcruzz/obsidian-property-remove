
# Obsidian Property Remove


This script allows you to remove specific properties from all Markdown files in an Obsidian vault. It's useful for cleaning up unwanted metadata or other properties that may have been added to your notes.

## How It Works

The script scans all `.md` files in your Obsidian vault, identifies the lines containing the property you wish to remove, and then rewrites the files without those lines.

## Requirements

- Python 3.x
- Access to your Obsidian vault path

## Setup

1. Clone the repository or download the script.

```bash
git clone https://github.com/pedrorcruzz/obsidian-property-remove.git
```

2. Run the script.

```bash
python3 main.py
```

## Features

- Set or edit the path to your Obsidian vault.
- Remove a specific property from all `.md` files in your vault.
- Option to return to the main menu during property removal.
- The property to remove must follow the format `property-name:` (including the colon).

## Example Usage

When running the script, you'll be presented with a menu to:

1. Set or edit the vault path.
2. Remove a property from the vault (if the vault is configured).
3. Exit the program.

The script will prompt you to enter the vault path and the property you want to remove.

***

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

