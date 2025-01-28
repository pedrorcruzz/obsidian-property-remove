import os

vault_path = os.path.expanduser("~/your/path")

property_to_remove = "name-property:"

for root, _, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            new_lines = [line for line in lines if property_to_remove not in line]
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

print("Property(ies) removed successfully!")
