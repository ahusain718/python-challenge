#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
import os

#establish connection to files
file_to_load = os.path.join("resources", "budget_data.csv")
file_to_output = os.path.join("python-challenge", "PyBank", "analysis", "budget_analysis")

#initialize variables
total_months = 0
total_net = 0
total_change = 0
average_change = 0
greatest_inc = 0
greatest_dec = 0


# In[21]:


with open(file_to_load) as financial_data:
    reader = list(csv.reader(financial_data))

    # Calculate total months
    for i in range(0, len(reader) - 1): 
        row = reader[i]
        next_row = reader[i + 1]

        if row != next_row:
                total_months += 1

    line1 = f"Total Months: {total_months}"


# In[25]:


# Calculate net total profit/loss
headers = reader[0]
col_index = headers.index('Profit/Losses')
column_data = [float(row[col_index]) 
    for row in reader[1:] if row[col_index]] 

total_net = round(sum(column_data))

line2 = f"Total: ${total_net}"


# In[27]:


# Calculate the average change in Profit/Losses over the period
for i in range(len(column_data) - 1):
    change = column_data[i + 1] - column_data[i]
    total_change += change
    average_change = total_change / (len(column_data) - 1)
   
line3 = f"Average Change: ${average_change:.2f}"


# In[29]:


headers = reader[0]
col_date = headers.index('Date')
date_data = [row[col_date] for row in reader[1:]]

# Calculate greatest inc and dec in profits
changes = [column_data[i + 1] - column_data[i] for i in range(len(column_data) - 1)]
greatest_inc = round(max(changes))
index_of_greatest_inc = changes.index(greatest_inc)

date_for_greatest_inc = date_data[index_of_greatest_inc + 1]
    
line4 = f"Greatest Increase in Profits: {date_for_greatest_inc} (${greatest_inc})"

greatest_dec = round(min(changes))
index_of_greatest_dec = changes.index(greatest_dec)

date_for_greatest_dec = date_data[index_of_greatest_dec + 1]
    
line5 = f"Greatest Decrease in Profits: {date_for_greatest_dec} (${greatest_dec})"


# In[31]:


#print to analysis.txt
title = "Financial Analysis"
dash_line = '-' * 30

lines = [
    title,
    dash_line,
    line1,
    line2,
    line3,
    line4,
    line5
]

with open('analysis/budget_analysis', 'w') as file:
    for line in lines:
        file.write(line + '\n')

