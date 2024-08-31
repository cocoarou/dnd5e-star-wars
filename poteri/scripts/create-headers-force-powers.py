import os

full_path = os.path.realpath(__file__)
os.path.dirname(full_path)

# Read the markdown table from an existing file
with open(os.getcwd() + '/poteri/scripts/test.md', 'r') as input_file:
    markdown_table = input_file.read()

# Split the table into lines
lines = markdown_table.strip().split('\n')

# Extract the first element of each row (excluding the header) and prepend ####
first_elements = [f"{line.split('|')[1].strip()}" for line in lines]
first_elements = [f"## {line.split('[')[1].split(']')[0].strip()}" for line in lines]


# Save the result into a new file
with open('first_elements_with_headers.txt', 'w') as output_file:
    for element in first_elements:
        output_file.write(element + '\n\n\n\n')

print("First elements with headers have been saved to 'first_elements_with_headers.txt'")

# import os

# print("Path at terminal when executing this file")
# print(os.getcwd() + "\n")

# print("This file path, relative to os.getcwd()")
# print(__file__ + "\n")

# print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")

# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

# print("This file directory only")
# print(os.path.dirname(full_path))