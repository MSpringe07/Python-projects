def add_mult(a, b, c):
    sorted_nums = sorted([a, b, c])
    return (sorted_nums[0] + sorted_nums[1]) * sorted_nums[2]

# Get input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Call the function and display the result
result = add_mult(a, b, c)
print(f"The result of add_mult is: {result}")
