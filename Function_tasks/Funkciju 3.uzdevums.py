import string

def extract_poetry_lines(filename):
    poetry_lines = []

    # Open and read the file
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            # Remove whitespace and check if the line isn't empty
            stripped_line = line.strip()
            if stripped_line:  # If line is not empty
                poetry_lines.append(line)

    return poetry_lines

def save_to_file(lines, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        for line in lines:
            file.write(line)

def remove_punctuation_and_save(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as file:
        content = file.read()
    cleaned_content = content.translate(str.maketrans('', '', string.punctuation))
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(cleaned_content)

# Name of the file to search in
input_filename = "/Users/mspringe4/Desktop/Python/veidenbaums.txt"
poetry_lines = extract_poetry_lines(input_filename)

output_filename_poems = "/Users/mspringe4/Desktop/Python/veidenbaums_poems.txt"
output_filename_no_punkts = "/Users/mspringe4/Desktop/Python/veidenbaums_no_punkts.txt"


# Save the poetry lines to a new file
if poetry_lines:
    save_to_file(poetry_lines, output_filename_poems)
    print("Poetry lines have been saved to veidenbaums_poems.txt!")
else:
    print("No poetry lines were found.")


remove_punctuation_and_save(output_filename_poems, output_filename_no_punkts)
print(f"Cleaned file has been saved to {output_filename_no_punkts}!")
