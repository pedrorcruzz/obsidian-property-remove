import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(SCRIPT_DIR, "config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

def set_vault_path():
    vault_path = os.path.expanduser(input("Enter the new path of your vault: ").strip())

    if not os.path.isdir(vault_path):
        print("Error: The specified path is not a valid directory.")
        return

    config = load_config()
    config["vault_path"] = vault_path
    save_config(config)
    print("Vault path saved successfully!")

def remove_property():
    config = load_config()
    vault_path = config.get("vault_path")

    if not vault_path:
        print("Error: No vault configured. Please configure the vault first.")
        return
    
    while True:
        property_to_remove = input("Enter the name of the property to remove (or type 'back' to return to the menu): ").strip()

        if property_to_remove.lower() == "back":
            return

        property_to_remove += ":"

        for root, _, files in os.walk(vault_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    new_lines = [line for line in lines if property_to_remove not in line]
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.writelines(new_lines)

        print(f"Property '{property_to_remove}' removed successfully!")

def main():
    while True:
        config = load_config()
        vault_path = config.get("vault_path", "Not configured")

        print("\n===== MENU =====")
        print(f"1. Add/Edit Vault Path (Current: {vault_path})")
        if "vault_path" in config:
            print("2. Remove Property from Obsidian")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            set_vault_path()
        elif choice == "2" and "vault_path" in config:
            remove_property()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
