# Get user input
user_input = input("Enter a value: ")

# Try to convert the input to different types and check the result
try:
    # Try converting to an integer
    value = int(user_input)
    print("Input is of type: Integer")
except ValueError:
    try:
        # Try converting to a float
        value = float(user_input)
        print("Input is of type: Float")
    except ValueError:
        # If not an integer or float, it's a string
        print("Input is of type: String")