def is_palindrome(text):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = ''.join(filter(str.isalpha, text)).lower()
    
    # Compare with its reverse
    return cleaned_text == cleaned_text[::-1]

# Get input from the user
text = input("Enter a word or sentence to check if it's a palindrome: ")

# Check if the input is a palindrome and display the result
if is_palindrome(text):
    print("The provided input is a palindrome.")
else:
    print("The provided input is not a palindrome.")
