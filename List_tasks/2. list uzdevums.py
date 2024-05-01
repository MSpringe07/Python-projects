def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def main():
    try:
        n = int(input("Enter the number of elements in the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        fibonacci_sequence = generate_fibonacci_sequence(n)
        print("Fibonacci Sequence:", fibonacci_sequence)

        y = int(input("Enter the position of the element you want (0-based index): "))
        if 0 <= y < len(fibonacci_sequence):
            print(f"The element at position {y} is {fibonacci_sequence[y]}.")
        else:
            print("Invalid position. Please enter a valid index within the sequence.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()






