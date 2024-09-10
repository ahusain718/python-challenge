#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import csv

# establish paths
file_to_load = os.path.join("resources", "election_data.csv")
file_for_output = os.path.join("analysis", "election_analysis")

# create variables
total_votes = 0
list_cand = []
votes_percand = {}
percentage_votes_percand = 0
winning_count = 0
winning_candidate = ""


# In[2]:


with open(file_to_load) as election_data:
    reader = list(csv.reader(election_data))
    headers = reader[0]

    #calculate total number of votes cast
    total_votes = len(reader) - 1 #subtract header row

    line2 = f"Total Votes: {total_votes}"


# In[3]:


#find complete list of candidates who recieved votes
for row in reader[1:]:
    candidate = row[2]

    if candidate not in list_cand:
        list_cand.append(candidate)
        votes_percand[candidate] = 0
    
    votes_percand[candidate] = votes_percand[candidate] + 1


# In[11]:


#calculate votes, percentage of votes, and print out winning candidate
total_lines = []
for candidate in votes_percand:
    votes = votes_percand.get(candidate)
    percentage_votes_percand = (float(votes) / float(total_votes))*100
    line3 = f"{candidate}: {percentage_votes_percand:.3f}% ({votes})\n"
    total_lines.append(line3)
    
    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate
        
line4 = f"Winner: {winning_candidate}"


# In[13]:


#print out to analysis.txt
title = "Election Results"
dash_line = '-' * 30

lines = [
    title,
    dash_line,
    line2,
    dash_line,
    "".join(total_lines),
    dash_line,
    line4,
    dash_line
]

with open('analysis/election_analysis', 'w') as file:
    for line in lines:
        file.write(line + '\n')

