import re
import os

def create_reference_links(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    reference_links = []
    for line in lines:
        # Extract the content of the last column (Prerequisiti)
        content = re.search(r'\|([^|]+)\s*$', line)

        # Ignore rows where the last column has a value of "-"
        if content and content.group(1).strip() != "-":
            # Create a reference link
            apex = "\'"
            reference_link = f"[{content.group(1).strip()}](./Descrizione%20Poteri%20della%20Forza.md#{content.group(1).strip().lower().replace(' ', '-').replace('(', '').replace(')', '').replace(apex, '')})"
            reference_links.append(reference_link)

    return reference_links

def update_markdown_file(file_path, reference_links):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    link_index = 0  # Track the index of reference_links

    for i, line in enumerate(lines):
        # Extract the content of the last column (Prerequisiti)
        content = re.search(r'\|([^|]+)\s*$', line)

        # Only update rows where the last column has a value other than "-"
        if content and content.group(1).strip() != "-":
            # Replace only the content of the last column (Prerequisiti) with the reference link
            updated_line = re.sub(r'\|([^|]+)\s*$', f"| {reference_links[link_index]}", line)
            link_index += 1  # Move to the next reference link
        else:
            updated_line = line  # Keep the line unchanged if no replacement is needed

        updated_lines.append(updated_line)

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Replace 'path_to_your_file.md' with the actual path to your markdown file
file_path = os.getcwd() + '/poteri/scripts/test.md'
reference_links = create_reference_links(file_path)
update_markdown_file(file_path, reference_links)