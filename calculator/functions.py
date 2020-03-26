"""
Author:         Chris Unice
Description:    This script contains all the helper functions used by the application
"""
# --- Imports ---
import numpy as np


# --- Classes ---
class Breakdown(object):
    def __init__(self, capital, loan_apr, hoa, property_tax_rate, cap_ex_rate, vacancy_rate,
                 property_mgt_rate, desired_profit, profit_is_percent=True):
        # Convert input percents to decimals
        loan_apr, property_tax_rate, cap_ex_rate, vacancy_rate, property_mgt_rate = map(
            lambda x: x/100.,
            [loan_apr, property_tax_rate, cap_ex_rate, vacancy_rate, property_mgt_rate]
        )
        if profit_is_percent:
            desired_profit = desired_profit / 100.

        # Instance attributes
        self.capital = capital
        self.loan_apr = loan_apr
        self.hoa = float(hoa)
        self.property_tax_rate = property_tax_rate
        self.cap_ex_rate = cap_ex_rate
        self.vacancy_rate = vacancy_rate
        self.property_mgt_rate = property_mgt_rate
        self.desired_profit = desired_profit
        self.profit_is_percent = profit_is_percent

        # Calculated attributes
        self.purchase_price = float(self.capital) / 0.2
        self.down_payment = self.purchase_price * 0.2
        # monthly
        self.home_insurance = (1200/456000 * self.purchase_price) / 12
        self.property_tax = (self.property_tax_rate * self.purchase_price) / 12
        self.principle_interest = -1 * np.pmt(self.loan_apr/12, 360, (self.purchase_price-self.down_payment))
        self.mortgage = self.principle_interest + self.hoa + self.home_insurance + self.property_tax
        if self.profit_is_percent:
            rate_sum = self.cap_ex_rate + self.vacancy_rate + self.property_mgt_rate + self.desired_profit
            self.required_rent = self.mortgage / (1 - rate_sum)
            self.profit_margin = self.required_rent * self.desired_profit
        else:
            rate_sum = self.cap_ex_rate + self.vacancy_rate + self.property_mgt_rate
            self.required_rent = (self.mortgage + self.desired_profit) / (1 - rate_sum)
            self.profit_margin = self.desired_profit
        self.cap_ex = self.required_rent * self.cap_ex_rate
        self.vacancy = self.required_rent * self.vacancy_rate
        self.property_mgt = self.required_rent * self.property_mgt_rate

        return None


# --- Functions ---
def format2number(x):
    return float(x.replace('$', '').replace(',', ''))
# end file
