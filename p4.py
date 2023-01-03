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
