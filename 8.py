# debugging



# raise Exception ('This is the error message.')

def divide_numbers(x, y):
    try:
        result = x / y  # Try to perform the division
    except ZeroDivisionError:  # Handle division by zero error
        raise ValueError("Cannot divide by zero")  # Raise a ValueError with a custom error message
    except TypeError:  # Handle type error (if arguments are not numbers)
        raise TypeError("Both arguments must be numbers")  # Raise a TypeError with a custom error message
    else:  # If no exceptions occurred
        return result  # Return the result of the division

try:
    quotient = divide_numbers(10, 5)  # Call the divide_numbers function with arguments 10 and 0
    print("Quotient:", quotient)  # Print the result
except ValueError as ve:  # Handle ValueError
    print("Error occurred:", ve)  # Print the error message
except TypeError as te:  # Handle TypeError
    print("Error occurred:", te)  # Print the error message


# AssertionError

x = 10
y = 0

try:
    assert y != 0  # Ensure y is not zero
    result = x / y
except AssertionError:
    print("Error: y cannot be zero")




# logging

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def divide_numbers(x, y):
    try:
        result = x / y  # Try to perform the division
    except ZeroDivisionError:  # Handle division by zero error
        logging.error("Cannot divide by zero")  # Log an error message
        raise ValueError("Cannot divide by zero")  # Raise a ValueError with a custom error message
    except TypeError:  # Handle type error (if arguments are not numbers)
        logging.error("Both arguments must be numbers")  # Log an error message
        raise TypeError("Both arguments must be numbers")  # Raise a TypeError with a custom error message
    else:  # If no exceptions occurred
        return result  # Return the result of the division

# Example usage:
try:
    quotient = divide_numbers(10, 0)  # Call the divide_numbers function with arguments 10 and 0
    logging.info("Quotient: %f", quotient)  # Log the result
except ValueError as ve:  # Handle ValueError
    logging.error("Error occurred: %s", ve)  # Log the error message
except TypeError as te:  # Handle TypeError
    logging.error("Error occurred: %s", te)  # Log the error message
