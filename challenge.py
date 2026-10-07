# Challenge Name: Smart Eligibility & Pricing System
"""
Build and demonstrate one complete path from input to final result.
Minimum challenge
• At least 3 inputs.
• At least 2 decision rules.
• At least one and/or/not expression.
• At least one calculation.
• A readable final message.
• At least 5 tests.
• At least one boundary failure found and fixed.
""" 

# INPUT
age = int(input("Enter age: "))
is_student = input("Are you a student? ")
number_of_tickets = int(input("Number of ticket bought: "))

# Variables
is_eligible = is_student == "yes"
price_per_ticket = 800.0
discount = 10 / 100

# Eligibility Check and Discount Calculation
if age >= 18 and (is_eligible and number_of_tickets >= 3):
    discount_price = (price_per_ticket * 90) / 100
    price = discount_price * number_of_tickets
else:
    price = number_of_tickets * price_per_ticket
print(price)