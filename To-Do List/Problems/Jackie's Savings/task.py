def final_deposit_amount(*interest_rate, amount=1000):
    for rate in interest_rate:
        amount = amount * (1 + rate / 100)
    return round(amount, 2)

