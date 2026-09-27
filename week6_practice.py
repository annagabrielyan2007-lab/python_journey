# WEEK 6: Functions & Data Flow

# 1. Defining a function with parameters and a return statement
def calculate_final_price(base_price, discount_percentage):
    """Calculates the final price after applying a percentage discount."""
    discount_amount = base_price * (discount_percentage / 100)
    final_price = base_price - discount_amount
    return final_price

# 2. Defining a function to format a greeting message
def generate_welcome_message(username, role="Guest"):
    """Returns a customized greeting message based on user role."""
    return f"Welcome back, {username}! Access level: {role}."

if __name__ == "__main__":
    print("--- WEEK 6: FUNCTIONS & DATA FLOW LAB ---\n")
    
    # Testing our calculation function
    item_price = 150.0
    discount = 20
    final = calculate_final_price(item_price, discount)
    print(f"Original Price: ${item_price}")
    print(f"Discount: {discount}%")
    print(f"Final Calculated Price: ${final}\n")
    
    # Testing our greeting function
    message = generate_welcome_message("Alex", "Administrator")
    print(message)