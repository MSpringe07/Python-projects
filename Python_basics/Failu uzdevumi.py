import re

def find_chapters_by_lines(file_path):
    chapter_info = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            if re.match(r'^\s*Chapter [IVXLCDM]+', line, re.IGNORECASE):
                chapter_title = line.strip()
                chapter_info.append((i, chapter_title))
    return chapter_info

def find_chapters_by_position(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        chapters = [(m.start(), m.group().strip()) for m in re.finditer(r'\bChapter [IVXLCDM]+\b', content, re.IGNORECASE)]
    return chapters

def print_chapters_in_rows(chapters, title):
    print(f"{title}:")
    print(f"{'Chapter':<15} {'Position/Line Number':<25}")
    print("-" * 40)
    for position, chapter in chapters:
        print(f"{chapter:<15} {position:<25}")
    print()

def main():
    file_path = 'pride_and_prejudice.txt'  # Replace with your actual file path
    output_path = 'chapter_info.txt'

    # Find chapters by lines
    chapters_by_lines = find_chapters_by_lines(file_path)

    # Find chapters by position
    chapters_by_position = find_chapters_by_position(file_path)

    # Write the results to a file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("Chapters by Line Number:\n")
        for line_number, title in chapters_by_lines:
            output_file.write(f"Line {line_number}: {title}\n")

        output_file.write("\nChapters by Position:\n")
        for position, title in chapters_by_position:
            output_file.write(f"Position {position}: {title}\n")

    # Print the results in the terminal as neatly arranged rows
    print_chapters_in_rows(chapters_by_lines, "Chapters by Line Number")
    print_chapters_in_rows(chapters_by_position, "Chapters by Position")

    print(f"Chapter information also written to {output_path}")

if __name__ == "__main__":
    main()
