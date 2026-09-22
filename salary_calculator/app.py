import os
from calculator import calculate_overtime_pay, calculate_progressive_tax

def get_float_input(prompt: str) -> float:
    """Repeatedly prompts for input until a valid positive number is provided."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid numeric input. Please enter numbers only.")

def main():
    print("==========================================")
    print("   SALARY & RATE CALCULATOR CLI (WEEK 4)  ")
    print("==========================================\n")

    # Collect inputs safely
    base_monthly_salary = get_float_input("Enter base monthly salary ($): ")
    hourly_rate = get_float_input("Enter standard hourly rate ($/hr): ")
    hours_worked = get_float_input("Enter total hours worked this month: ")

    # Compute calculations
    overtime_pay = calculate_overtime_pay(hours_worked, hourly_rate, standard_hours=160.0)
    gross_pay = base_monthly_salary + overtime_pay
    total_tax, tax_breakdown = calculate_progressive_tax(gross_pay)
    net_pay = gross_pay - total_tax
    effective_hourly_rate = net_pay / hours_worked if hours_worked > 0 else 0.0

    # Format output summary
    summary = f"""
------------------------------------------
            PAYROLL BREAKDOWN             
------------------------------------------
Base Salary:            ${base_monthly_salary:,.2f}
Overtime Pay:           ${overtime_pay:,.2f}
Gross Pay:              ${gross_pay:,.2f}

--- Tax Deductions ---
"""
    for line in tax_breakdown:
        summary += f"{line}\n"

    summary += f"""Total Tax Deducted:     ${total_tax:,.2f}
------------------------------------------
NET EARNINGS:           ${net_pay:,.2f}
Effective Hourly Value: ${effective_hourly_rate:,.2f}/hr
------------------------------------------
"""

    print(summary)

    # Save to text file
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/summary.txt", "w") as f:
        f.write(summary)
    
    print("Summary report successfully saved to 'outputs/summary.txt'.")

if __name__ == "__main__":
    main()