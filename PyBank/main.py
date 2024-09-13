#!/usr/bin/env python
# coding: utf-8

# In[488]:


import csv
import os

#establish connection to files
file_to_load = os.path.join("python-challenge", "PyBank", "resources", "budget_data.csv")

total_months = 0
total_net = 0
total_change = 0
average_change = 0
greatest_inc = 0
greatest_dec = 0
#QUESTION - what is the difference between setting variables as 0 vs as []?


# In[490]:


with open(file_to_load) as financial_data:
    reader = list(csv.reader(financial_data))

    #QUESTION - if I remove this section why does it list total_months rather than state it as 1 number?
    if len(reader) < 2:
        print("Not enough data to compare rows.")
    else:
        total_months = 0  

        # Calculate total months
        #QUESTION - how do I know this is looking at first column data?
        for i in range(0, len(reader) - 1): 
            row = reader[i]
            next_row = reader[i + 1]

            if row != next_row:
                total_months += 1

        line1 = f"Total Months: {total_months}"


# In[500]:


#Calculate net total profit/loss
headers = reader[0]
col_index = headers.index('Profit/Losses')
column_data = [float(row[col_index]) 
    for row in reader[1:] if row[col_index]] #QUESTION - not sure what this does?

# Calculate the total of the specified column
total_net = sum(column_data)

line2 = f"Total: ${total_net}"


# In[494]:


#Calculate the average change in Profit/Losses over the period
for i in range(len(column_data) - 1):
    change = column_data[i + 1] - column_data[i]
    total_change += change
    average_change = total_change / (len(column_data) - 1)
    #QUESTION if the total months number is incorrect why is this number showing up correctly?

line3 = f"Average Change: ${average_change:.2f}"


# In[496]:


headers = reader[0]
col_date = headers.index('Date')
date_data = [row[col_date] for row in reader[1:]]

changes = [column_data[i + 1] - column_data[i] for i in range(len(column_data) - 1)]
greatest_inc = max(changes)
index_of_greatest_inc = changes.index(greatest_inc)

date_for_greatest_inc = date_data[index_of_greatest_inc + 1]
    
line4 = f"Greatest Increase in Profits: {date_for_greatest_inc} (${greatest_inc})"

greatest_dec = min(changes)
index_of_greatest_dec = changes.index(greatest_dec)

date_for_greatest_dec = date_data[index_of_greatest_dec + 1]
    
line5 = f"Greatest Decrease in Profits: {date_for_greatest_dec} (${greatest_dec})"
            


# In[502]:


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

#QUESTION - why is this not being uploaded to the correct folder?
file_to_output = os.path.join("python-challenge", "PyBank", "analysis", "budget_analysis.txt")
with open('budget_analysis.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')


# In[ ]:


#Print to terminal
print(title)
print(dash_line)
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)

