# -*- coding: utf-8 -*-

import math

def simulate(borrowing, repayment):
    month = 0
    payment = 0
    capital = 0
    interest = 0
    balance = borrowing
    interest_amount = 0
    payment_amount = 0
    result = {}
    result_list = []

    month = int(math.ceil(borrowing / repayment))
    result["month"] = month

    for i in range(month):
        if i == month - 1:
            capital = borrowing - repayment * i
        else:
            capital = repayment

        interest = int(balance * 0.15 / 12)
        payment = capital + interest
        balance -= capital

        result_list.append([i + 1, payment, capital, interest, balance])

        interest_amount += interest
        payment_amount += payment

    result["interest_amount"] = interest_amount
    result["payment_amount"] = payment_amount

    return (result, result_list)
