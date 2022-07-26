"""
    Author:   Drew Herrera
    Date:     06/16/2022
    Version:  1.0
    Purpose:  Loan portfolio analysis through automation
"""
# File imports
import csv
from pathlib import Path


def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    """ Calculates the present value of a loan.
    
    Args:
        future_value (float): The future value of the loan
        remaining_months (int): The remaining months left to pay off the loan
        annual_discount_rate (float): The discount rate of the loan

    Returns:
        The present value of the loan
        
    """
    present_value = future_value / (1 + annual_discount_rate/12)**remaining_months
    return present_value


"""Part 1: Automate the Calculations.

    Automate the calculations for the loan portfolio summaries.

"""
# Given a list of loan costs
loan_costs = [500, 600, 200, 1000, 450]

# Calculate the total number of loans
total_number_of_loans = len(loan_costs)

# Print the number of loans
print(f"Number of loans is: {total_number_of_loans}")

# Sum the total cost of all loans
sum_of_loan_costs = sum(loan_costs)

# Print the sum
print(f"Sum of all loans is: ${sum_of_loan_costs}")

# Calculate the average loan price
average_loan_price = sum_of_loan_costs / total_number_of_loans

# Print the average loan price
print(f"Average loan price is: ${average_loan_price}")


"""Part 2: Analyze Loan Data.

    Analyze the loan to determine the investment evaluation.

"""
# Given a loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Retrieve future value of the loan
future_value = loan.get("future_value")

# Retrieve remaining months of the loan
remaining_months = loan.get("remaining_months")

# Print the future value of the loan
print(f"future_value is: {future_value}")

# Print the remaining months on the loan
print(f"remaining_months is: {remaining_months}")

# Calculate the present value
# Note: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = future_value / (1 + .20/12)**remaining_months

# Print the present value
print(f"present_value is: {round(present_value, 2)}")

# Retrieve the price of the loan
loan_price = loan.get("loan_price")

# Print the loan price
print(f"loan_price = {loan_price}")

# Determine if the present value of the loan represents the loan's fair value
if present_value >= loan_price:
    print(f"The loan is worth at least the cost to buy it!")
else:
    print(f"The loan is too expensive and not worth the price!")


"""Part 3: Perform Financial Calculations.

    Perform financial calculations using functions.

"""
# Given a new loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Given discounted rate 
annual_discount_rate = 0.20

# Retrieve future value
future_value = new_loan.get("future_value")

# Retrieve remaining months
remaining_months = new_loan.get("remaining_months")

# Print annual discounted rate
print(f"annual_discount_rate is: {annual_discount_rate}")

# Print future value
print(f"future_value is: ${future_value}")

# Print remaining months
print(f"remaining_months is: {remaining_months}")

# Calculate present value of the loan
present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate)

# Print the present value of the loan
print(f"The present value of the loan is: ${round(present_value, 2)}")


"""Part 4: Conditionally filter lists of loans.

    Identify inexpensive loans
"""
# Given a list of loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Define list of inexpensive loans
inexpensive_loans = []

# Loans with price less than or equal to 500 are listed as an inexpensive
for loan in loans:
    loan_price = loan.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(loan)
    

# Print the list of inexpensive loans
print(f"The inexpensive loans are: {inexpensive_loans}")


"""Part 5: Save the results.

    Output list of inexpensive loans to a csv file

"""
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file pathls
output_path = Path("inexpensive_loans.csv")

# Write out each inexpensive loan to a .csv file
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
