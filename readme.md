### Piotr Malec 318544

# LAB 4 task 2

# Inputs

* credit_amount
* interest_rate
* banks_fee
* payment_period

# Outputs

* capital_installment
* interest_installment
* total_installment
* total_cost

# How it works?

User must provide some data about loan:

 * Credit amount
 * Interest rate
 * Bank's fee
 * Period of time 


Then program calculate each part of installment and the total amount of money deposited into the bank already.

The last step is to display this data in a table.

# Necessary packages
from rich.table import Table
from rich.console import Console
from rich.prompt import FloatPrompt
from rich.prompt import IntPrompt

# Rules of usage

Each input data must be a number

# Exemplary results

The image "RESULTS.jpg" shows the usage and the result is in this repository.
