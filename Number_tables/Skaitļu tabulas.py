def calculate_missing_value(row):
    a, b, a2b, ab2 = row
    if a == 0 and b != 0:
        a = a2b / (b ** 2) if b ** 2 != 0 else -1
    elif b == 0 and a != 0:
        b = a2b / (a ** 2) if a ** 2 != 0 else -1
    elif a2b == 0 and a != 0 and b != 0:
        a2b = a ** 2 * b
    elif ab2 == 0 and a != 0 and b != 0:
        ab2 = a * b ** 2
    return [a, b, a2b, ab2]

def format_number(num):
    # Assuming num is already a float
    return str(int(num)) if num.is_integer() else f"{num:.2f}"

def format_row(row, column_widths):
    # Convert numbers to strings, applying formatting
    formatted_row = [format_number(num).rjust(width) for num, width in zip(row, column_widths)]
    return '     '.join(formatted_row)

def get_column_widths(data_lines, header_columns):
    column_widths = [len(col) for col in header_columns]
    for line in data_lines:
        for index, number in enumerate(line.split()):
            column_widths[index] = max(column_widths[index], len(format_number(float(number))))
    return column_widths

def process_data(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    header = lines[0].strip()
    data_lines = lines[1:]
    header_columns = header.split()
    column_widths = get_column_widths(data_lines, header_columns)

    with open(output_file, 'w') as outfile:
        # Here, the header should be written out without changes
        outfile.write(header + '\n')
        
        for line in data_lines:
            row = [float(num) for num in line.split()]
            calculated_row = calculate_missing_value(row)
            formatted_row = format_row(calculated_row, column_widths)
            outfile.write(formatted_row + '\n')

def main():
    input_file = 'inputdata.txt'
    output_file = 'outputdata.txt'
    process_data(input_file, output_file)
    print(f"Processed data has been saved to {output_file}")

if __name__ == "__main__":
    main()
