"""
Author:         Chris Unice
Description:    This script contains all the helper functions used by the application
"""
# --- Imports ---
import numpy as np


# --- Functions ---
def format2number(x):
    return float(x.replace('$', '').replace(',', ''))


def calculate_breakdown(capital, tax_rate, cap_rate, vac_rate, mgt_rate, profit_rate):
    # Check rates to be less than 1
    tax_rate, cap_rate, vac_rate, mgt_rate, profit_rate = map(
        lambda x: x/100. if x >= 1 else x,
        [tax_rate, cap_rate, vac_rate, mgt_rate, profit_rate]
    )

    # Hard code the loan APR for now
    loan_rate = 0.05

    # Parameters
    pp = capital / 0.2                          # purchase price
    loan = pp * 0.8                             # amount financed
    ins = (1200/456000 * pp)/12                 # home insurance
    re_tax = (tax_rate * pp)/12                 # real estate tax
    pi = -1*np.pmt(loan_rate/12, 360, loan)     # principle and interest
    m = pi + ins + re_tax                       # mortgage

    # Rent 1: based on getting 10% profit
    rent_1 = m / (1-(cap_rate + vac_rate + mgt_rate + profit_rate))
    # Rent 2: based on getting $100 profit
    rent_2 = (m + 100) / (1-(cap_rate + vac_rate + mgt_rate))
    # True Rent: we want the lesser of the two options
    rent = np.min([rent_1, rent_2])

    cap_amount = rent * cap_rate        # capital expenditure
    vac_amount = rent * vac_rate        # vacancy rate
    mgt_amount = rent * mgt_rate        # property management
    profit_amount = rent - (m + cap_amount + vac_amount + mgt_amount)   # profit margin

    return [cap_amount, vac_amount, mgt_amount, profit_amount, rent]
# end file
