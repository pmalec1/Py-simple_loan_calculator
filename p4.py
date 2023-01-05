from rich.table import Table
from rich.console import Console
from rich.prompt import FloatPrompt
from rich.prompt import IntPrompt


def get_inputs_from_user():
    print("Amount of credit[zl]: ")
    credit_amount = FloatPrompt.ask()   # kwota kredytu
    print("Interest rate[%]: ")
    interest_rate = FloatPrompt.ask()   # oprocentowanie roczne
    print("Bank's fee[%]: ")            # prowizja banku
    banks_fee = FloatPrompt.ask()
    print("Number of credit years: ")   # okres splaty
    payment_period = IntPrompt.ask()
    credit_informations = {'Credit amount': credit_amount, 'Interest rate': interest_rate,
                           'Banks fee': banks_fee, 'Payment period': payment_period}
    return credit_informations


def calculate_interest_intallment(total_credit_amount, number_of_month, capital_installment, provision_per_year):
    interest_installment = ((total_credit_amount-number_of_month*capital_installment)*provision_per_year)/12
    return round(interest_installment, 2)


def calculate_capital_installment(total_credit_amount, amount_of_months):
    capital_installment = total_credit_amount / amount_of_months
    return round(capital_installment, 2)


def calculate_total_installment(interest_intallment, capital_installment):
    total_installment = interest_intallment+capital_installment
    return round(total_installment, 2)
