try:
    from rich.table import Table
    from rich.console import Console
    from rich.prompt import FloatPrompt
    from rich.prompt import IntPrompt
except:
    print("\n!Module rich is not installed!\n!Try to install it using pip -packages manager!\n")
    exit(0)


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


def calculate_capital_installment(total_credit_amount, amount_of_months):
    capital_installment = total_credit_amount / amount_of_months
    return round(capital_installment, 2)


def calculate_interest_intallment(total_credit_amount, number_of_month, capital_installment, provision_per_year):
    interest_installment = ((total_credit_amount-number_of_month*capital_installment)*provision_per_year)/12
    return round(interest_installment, 2)


def calculate_total_installment(interest_intallment, capital_installment):
    total_installment = interest_intallment+capital_installment
    return round(total_installment, 2)


def add_row_of_elements_to_list_of_installments(list_of_installments, m, current_payment_status_data):
    for n in range(5):
        list_of_installments[m].append(current_payment_status_data[n])


def update_informations_about_last_payment(m, p, x, capital_installment):
    number_of_payment = m + 1
    interest_installment = calculate_interest_intallment(p, m, capital_installment, x)
    total_installment = calculate_total_installment(interest_installment, capital_installment)
    return [number_of_payment, capital_installment, interest_installment, total_installment]


def calculate_how_much_already_paid(current_payment_status, total_cost):
    return round(total_cost + current_payment_status[3], 2)


def mortage_calculator(credit_informations):

    p = credit_informations['Credit amount'] * (1 + credit_informations['Banks fee'] / 100)
    x = credit_informations['Interest rate'] / 100
    n = credit_informations['Payment period'] * 12
    capital_installment = calculate_capital_installment(p, n)
    list_of_installments = [[] for n in range(n)]
    total_cost = 0
    for m in range(n):
        current_payment_status_data = update_informations_about_last_payment(m, p, x, capital_installment)
        total_cost = calculate_how_much_already_paid(current_payment_status_data, total_cost)
        current_payment_status_data.append(total_cost)
        add_row_of_elements_to_list_of_installments(list_of_installments, m, current_payment_status_data)
    return list_of_installments


def print_table_of_installments_informations(list_of_installments):
    table = Table(title="Statistics of mortage credit payments")
    table.add_column("Number of payment")
    table.add_column("Capital Installment")
    table.add_column("Interest Installment")
    table.add_column("Total Installment")
    table.add_column("Total cost of credit")
    for m in range(len(list_of_installments)):
        table.add_row(str(list_of_installments[m][0]), str(list_of_installments[m][1]), str(list_of_installments[m][2]),
                      str(list_of_installments[m][3]), str(list_of_installments[m][4]))
    console = Console()
    console.print(table)


def main():
    credit_data = get_inputs_from_user()
    list_of_installments = mortage_calculator(credit_data)
    print_table_of_installments_informations(list_of_installments)


if __name__ == "__main__":
    main()
