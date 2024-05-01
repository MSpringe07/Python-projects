def is_valid_input(input_string):
    segments = input_string.split(', ')
    
    # Check if every segment is numeric.
    for segment in segments:
        if not segment.strip().isdigit():
            return False
            
    # Ensure the only separators used are ", "
    if ', ' not in input_string:
        return False

    if ',,' in input_string or input_string.startswith(',') or input_string.endswith(','):
        return False
            
    return True

def get_input_from_user():
    while True:
        # Prompt the user to enter a comma-separated list of numbers.
        input_string = input("Enter a list of natural numbers separated by ', ' pay attention to syntax: ")
        if is_valid_input(input_string):
            # Split the string by ', ' and convert each segment to an integer.
            numbers = [int(x) for x in input_string.split(', ')]
            return numbers
        else:
            print("Entered string is not valid! Please try again.")

def longest_substring(numbers):
    # Using two pointers to define the sliding window: start and end.
    start, end = 0, 0
    # Using a set to store the numbers in the current window.
    current_numbers = set()
    max_length = 0
    fragments = []

    while end < len(numbers):
        if numbers[end] not in current_numbers:
            current_numbers.add(numbers[end])
            end += 1
            if end - start > max_length:
                max_length = end - start
                fragments = [start] # Reset the fragments list with the new start.
            elif end - start == max_length:
                fragments.append(start) # Add the current start to fragments.
        else:
            current_numbers.remove(numbers[start])
            start += 1

    # Use the fragments list to extract the actual number sequences.
    return [numbers[i:i+max_length] for i in fragments]

def main():
    numbers = get_input_from_user()
    if numbers is None:
        return
    result = longest_substring(numbers)
    print("Longest fragments with unique numbers:", result)

main()
