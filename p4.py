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


def mortage_calculator(credit_informations):

    p = credit_informations['Credit amount'] * (1 + credit_informations['Banks fee'] / 100)
    x = credit_informations['Interest rate'] / 100
    n = credit_informations['Payment period'] * 12

    capital_installment = calculate_capital_installment(p, n)
    list_of_installments = [[] for n in range(n)]
    total_cost = 0

    for m in range(n):
        number_of_payment = m+1
        interest_installment = calculate_interest_intallment(p, m, capital_installment, x)
        total_installment = calculate_total_installment(interest_installment, capital_installment)
        total_cost = round(total_cost + total_installment, 2)
        list_of_installments[m].append(number_of_payment)
        list_of_installments[m].append(capital_installment)
        list_of_installments[m].append(interest_installment)
        list_of_installments[m].append(total_installment)
        list_of_installments[m].append(total_cost)
    return list_of_installments


def make_table_of_installments_informations(list_of_installments):
    table = Table(title="Statistics of mortage credit payments")
    table.add_column("Number of payment", justify="right")
    table.add_column("Capital Installment", justify="right")
    table.add_column("Interest Installment", justify="right",)
    table.add_column("Total Installment", justify="right",)
    table.add_column("Total cost of credit", justify="right",)
    for m in range(len(list_of_installments)):
        table.add_row(str(m + 1), str(list_of_installments[m][1]), str(list_of_installments[m][2]),
                      str(list_of_installments[m][3]), str(list_of_installments[m][4]))
    console = Console()
    console.print(table)


credit_data = get_inputs_from_user()
list_of_installments = mortage_calculator(credit_data)
make_table_of_installments_informations(list_of_installments)
