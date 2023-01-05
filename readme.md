### Piotr Malec 318544

# LAB 4 task 2

# Inputs

* credit_amount --[zl]total amount of credit (include bank's provison)
* interest_rate -- [%]
* banks_fee     -- [%]banks provision
* payment_period --[years] number of credit years

# Outputs

* capital_installment  --constant part of installment
* interest_installment --variable part of installment
* total_installment    -- sum of capital_installment and interest_installment
* total_cost           -- mount of money deposited into the bank already

# Functions
1. get_inputs_from_user(): --> collecting data about loan (returns credit infomations)
2. calculate_interest_intallment(total_credit_amount, number_of_month, --->capital_installment, provision_per_year) --calculate variable part of installment
3. calculate_capital_installment(total_credit_amount, amount_of_months):---> calculate constant part of installment (only once)
4. calculate_total_installment(interest_intallment, capital_installment):--->sum of each part of installment
5. mortage_calculator(credit_informations):---> returns list of installments
6. make_table_of_installments_informations(list_of_installments):---> make a table with list of installments

# How it works?

1. User must provide some data about loan:

 * Credit amount
 * Interest rate
 * Bank's fee
 * Period of time 

  
2.  Then program calculate each part of installment and the total amount of money deposited into the bank already.

3. The last step is to display this data in a table.

# Necessary packages
* from rich.table import Table
* from rich.console import Console
* from rich.prompt import FloatPrompt
* from rich.prompt import IntPrompt

# Rules of usage

Each input data must be a number

# Exemplary results

The image "EXEMPLARY_RESULTS" shows the usage and the result is in this repository.
