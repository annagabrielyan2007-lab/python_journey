# WEEK 6/7: Error Handling & Defensive Programming

def divide_numbers(numerator, denominator):
    """Safely divides two numbers, handling division by zero and invalid types."""
    try:
        # Attempt the risky operation
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except ValueError:
        return "Error: Please enter valid numbers only!"
    else:
        # Runs only if no exceptions occurred
        return f"Success! Result: {result}"
    finally:
        print("(Division operation completed)")

if __name__ == "__main__":
    print("--- WEEK 7: ERROR HANDLING LAB ---\n")
    
    # Test 1: Normal division
    print("Test 1 (10 / 2):")
    print(divide_numbers(10, 2))
    print()
    
    # Test 2: Division by zero
    print("Test 2 (10 / 0):")
    print(divide_numbers(10, 0))
    print()
    
    # Test 3: Invalid text input
    print("Test 3 ('ten' / 2):")
    print(divide_numbers("ten", 2))