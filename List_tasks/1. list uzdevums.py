def main():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            number = float(user_input)
            numbers.append(number)
            average = calculate_average(numbers)
            top3, bottom3 = get_top_and_bottom_numbers(numbers)
            display_numbers(numbers, average, top3, bottom3)
        except ValueError:
            print("Invalid input. Please enter a valid float number.")
    
    print("You've quit the program.")
    
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_top_and_bottom_numbers(numbers):
    sorted_numbers = sorted(numbers)
    top3 = sorted_numbers[-3:]
    bottom3 = sorted_numbers[:3]
    return top3, bottom3

def display_numbers(numbers, average, top3, bottom3):
    print("Input numbers: ", numbers)
    print(f"Average value: {average}\n")
    print("Top 3 numbers: {}".format(top3))
    print("Bottom 3 numbers: {}".format(bottom3))
    print()
    
if __name__ == "__main__":
    main()