import re
import os

def create_reference_links(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    reference_links = []
    for line in lines:
        # Extract the content of the first column
        content = re.search(r'\|(.*?)\|', line).group(1)

        # Create a reference link
        apex = "\'"
        reference_link = f"[{content}](./Descrizione%20Poteri%20della%20Forza.md#{content.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(apex, '')})"
        reference_links.append(reference_link)

    return reference_links

def update_markdown_file(file_path, reference_links):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for i, line in enumerate(lines):
        # Replace only the content of the first column with the reference link
        updated_line = re.sub(r'\|(.*?)\|', f'|{reference_links[i]}|', line, count=1)
        updated_lines.append(updated_line)

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Replace 'path_to_your_file.md' with the actual path to your markdown file
file_path = os.getcwd() + '/poteri/scripts/test.md'
reference_links = create_reference_links(file_path)
update_markdown_file(file_path, reference_links)