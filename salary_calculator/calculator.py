def calculate_overtime_pay(hours_worked: float, hourly_rate: float, standard_hours: float = 160.0, multiplier: float = 1.5) -> float:
    """Calculates earnings from hours worked beyond standard hours."""
    if hours_worked <= standard_hours:
        return 0.0
    overtime_hours = hours_worked - standard_hours
    return overtime_hours * (hourly_rate * multiplier)

def calculate_progressive_tax(gross_pay: float) -> tuple[float, list[str]]:
    """
    Applies a tiered tax rate to the gross pay:
    - First $1,000: 0% tax (Tax-free allowance)
    - $1,001 to $3,000: 10% tax
    - $3,001+: 20% tax
    Returns total tax and a list of breakdown descriptions.
    """
    tax = 0.0
    breakdown = []
    
    # Tier 1: 0% tax
    if gross_pay > 1000:
        tier1_taxable = 1000.0
    else:
        tier1_taxable = gross_pay
    breakdown.append(f"Tier 1 ($0 - $1,000 @ 0%): ${tier1_taxable * 0.00:.2f}")

    # Tier 2: 10% tax
    if gross_pay > 1000:
        tier2_taxable = min(gross_pay - 1000.0, 2000.0)
        t2_tax = tier2_taxable * 0.10
        tax += t2_tax
        breakdown.append(f"Tier 2 ($1,001 - $3,000 @ 10%): ${t2_tax:.2f}")

    # Tier 3: 20% tax
    if gross_pay > 3000:
        tier3_taxable = gross_pay - 3000.0
        t3_tax = tier3_taxable * 0.20
        tax += t3_tax
        breakdown.append(f"Tier 3 ($3,001+ @ 20%): ${t3_tax:.2f}")

    return tax, breakdown