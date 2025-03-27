#######################################################################################################################################################
# 
# Name:Priyanka Sharma
# SID:740098979
# Exam Date:27/03/2025
# Module:BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-Priya-exeter
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
allocated_keys = [7, 9]
my_list = [] # Initializing an empty list.

# Using for loop to traverse  through the allocated keys and find the start and end positions of each corresponding word.
for key in allocated_keys:
    # Retrieve the word from key_comments using the current key.
    word = key_comments[key]
    start_index = customer_feedback.find(word)
    
    # If statement for finding the word and to  calculate the end index.
    if start_index != -1:
        end_index = start_index + len(word) - 1
    else:
        # If not found, set end_index to -1 as well.
        end_index = -1
    my_list.append((start_index, end_index))
print(my_list)

#output - [(129, 135), (82, 86)]


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:79

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value average_order_value = calculate_average_order_value(
    total_revenue=first_two_digits, 
    total_orders=last_two_digits
)


first_two_digits = 74  # First two digits of student ID
last_two_digits = 79   # Last two digits of student ID

# Step 2: Create functions to calculate different financial metrics

def calculate_operating_profit_margin(operating_profit, total_revenue):
   if total_revenue == 0:
        return "Cannot calculate: Revenue is zero"
    margin = (operating_profit / total_revenue) * 100
    return margin

def calculate_revenue_per_customer(total_revenue, total_customers):
    
    if total_customers == 0:
        return "Cannot calculate: No customers"
    revenue_per_customer = total_revenue / total_customers
    return revenue_per_customer

def calculate_customer_churn_rate(customers_lost, total_customers):
    if total_customers == 0:
        return "Cannot calculate: No customers"

    churn_rate = (customers_lost / total_customers) * 100
    return churn_rate

def calculate_average_order_value(total_revenue, total_orders):
    
    if total_orders == 0:
        return "Cannot calculate: No orders"
    
   
    average_order_value = total_revenue / total_orders
    return average_order_value


operating_profit_margin = calculate_operating_profit_margin(
    operating_profit=first_two_digits, 
    total_revenue=last_two_digits
)
revenue_per_customer = calculate_revenue_per_customer(
    total_revenue=first_two_digits, 
    total_customers=last_two_digits
)
customer_churn_rate = calculate_customer_churn_rate(
    customers_lost=first_two_digits, 
    total_customers=last_two_digits
)

average_order_value = calculate_average_order_value(
    total_revenue=first_two_digits, 
    total_orders=last_two_digits
)
print("\n--- E-Commerce Weekly Financial Report ---")
print("=" * 40)


print(f"1. Operating Profit Margin: {operating_profit_margin:.2f}%" 
      if isinstance(operating_profit_margin, float) else 
      f"1. Operating Profit Margin: {operating_profit_margin}")

print(f"2. Revenue per Customer: ${revenue_per_customer:.2f}" 
      if isinstance(revenue_per_customer, float) else 
      f"2. Revenue per Customer: {revenue_per_customer}")

print(f"3. Customer Churn Rate: {customer_churn_rate:.2f}%" 
      if isinstance(customer_churn_rate, float) else 
      f"3. Customer Churn Rate: {customer_churn_rate}")

print(f"4. Average Order Value: ${average_order_value:.2f}" 
      if isinstance(average_order_value, float) else 
      f"4. Average Order Value: {average_order_value}")


print("\n--- Key learning ---")
print("* These metrics help understand business performance")
print("* Always check for potential division by zero")
print("* Context is crucial when interpreting these numbers")

#output- --- E-Commerce Weekly Financial Report ---
========================================
1. Operating Profit Margin: 93.67%
2. Revenue per Customer: $0.94
3. Customer Churn Rate: 93.67%
4. Average Order Value: $0.94

--- Key learning ---
* These metrics help understand business performance
* Always check for potential division by zero
* Context is crucial when interpreting these numbers

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""


# Write your code here
import numpy as np
import matplotlib.pyplot as plt
prices = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
demands = [300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85]

# Converting the  lists to numpy arrays for easy use of numpy library

prices_array = np.array(prices)
demands_array = np.array(demands)

# Using linear regression for  the relationship between price and demand and also use stratight line by using degree
slope, intercept = np.polyfit(prices_array, demands_array, deg=1)
print("Understanding Price and Demand:")
print("Our mathematical model says:")
print(f"Demand = {intercept:.2f} + ({slope:.2f}) * Price")
#Find the price that makes the most money (maximum revenue) that is optimal 
optimal_price = -intercept / (2 * slope)
optimal_revenue = optimal_price * (intercept + slope * optimal_price)

# Check demand at a specific price
test_price = 52
demand_at_test_price = intercept + slope * test_price
print("\nBusiness Insights:")
print(f"1. Best Price to Maximize Revenue: £{optimal_price:.2f}")
print(f"   This would generate revenue of about £{optimal_revenue:.2f}")
print(f"2. Expected Demand at £52: {demand_at_test_price:.2f} units")

#visualising graph by matplotlib

plt.figure(figsize=(10, 6))
plt.scatter(prices, demands, color='blue', label='Actual Data')
plt.plot(prices_array, intercept + slope * prices_array, color='red', label='Prediction Line')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Price vs Demand Analysis')
plt.legend()
plt.grid(True)
plt.show()


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

#Answer 
import random
import matplotlib.pyplot as plt

# Generating 100 random numbers between 1 and my student id : 740098979
# Using variable max_value and converting the input string to an integer.
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(100)] # To generate random nmbers

# Plot the random numbers on a line chart.
plt.plot(random_numbers,
         marker='O',               
         markerfacecolor='green',  
         markeredgecolor='red',   
         linestyle='--',          
         label='Random Numbers',   
         color='blue')             
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()