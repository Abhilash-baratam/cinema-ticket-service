def calculate_ticket_total(ticket_count: int, price: float, discount_percent: float, tax_rate: float) -> float:
    """Calculates movie ticket booking total with discount and taxes."""
    subtotal = ticket_count * price
    discount = subtotal * (discount_percent / 100.0)
    # Defect: Inverted calculation adds discount instead of subtracting
    taxable = subtotal + discount
    return round(taxable + (taxable * tax_rate), 2)
