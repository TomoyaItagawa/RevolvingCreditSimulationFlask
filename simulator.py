# -*- coding: utf-8 -*-

import math
from enum import Enum

class PaymentType(Enum):
    FIXED_RATE = 1
    FIXED_CAPITAL = 2

rate = 0.15

def simulate(payment_type, borrowing, repayment):
    if payment_type == PaymentType.FIXED_RATE.value:
        return __simulate_fixed_rate(borrowing, repayment)
    elif payment_type == PaymentType.FIXED_CAPITAL.value:
        return __simulate_fixed_capital(borrowing, repayment)
    else:
        return (None, None)

def __simulate_fixed_rate(borrowing, repayment):
    month = 0
    payment = 0
    capital = 0
    interest = 0
    balance = borrowing
    interest_amount = 0
    payment_amount = 0
    result = {}
    result_list = []

    i = 0
    while(balance > 0):
        if i >= 1000:
            month = 1001
            break

        interest = int(balance * rate / 12)
        if balance + interest > repayment:
            payment = repayment
        else:
            payment = balance + interest

        capital = payment - interest
        balance -= capital
        result_list.append([i + 1, payment, capital, interest, balance])

        interest_amount += interest
        payment_amount += payment
        month += 1
        i += 1

    result["interest_amount"] = interest_amount
    result["payment_amount"] = payment_amount
    result["month"] = month

    return (result, result_list)

def __simulate_fixed_capital(borrowing, repayment):
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
        elif i >= 1000:
            result["month"] = 1001
            break
        else:
            capital = repayment

        interest = int(balance * rate / 12)
        payment = capital + interest
        balance -= capital

        result_list.append([i + 1, payment, capital, interest, balance])

        interest_amount += interest
        payment_amount += payment

    result["interest_amount"] = interest_amount
    result["payment_amount"] = payment_amount

    return (result, result_list)
