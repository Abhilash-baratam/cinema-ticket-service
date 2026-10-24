from tickets import calculate_ticket_total

def test_ticket_checkout_calculation():
    # 2 tickets @ 200.0 = 400.0. 10% discount = 40.0 off -> 360.0 taxable. 5% tax = 18.0 -> Expected 378.0
    total = calculate_ticket_total(2, 200.0, 10.0, 0.05)
    assert total == 378.0, f"Expected 378.0, but got {total}"
