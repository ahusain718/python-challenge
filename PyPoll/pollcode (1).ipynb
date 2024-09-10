{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e61e2f4c-2cb0-45ea-bbde-063e8f98936e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os \n",
    "import csv\n",
    "\n",
    "# establish paths\n",
    "file_to_load = os.path.join(\"resources\", \"election_data.csv\")\n",
    "file_for_output = os.path.join(\"analysis\", \"election_analysis\")\n",
    "\n",
    "# create variables\n",
    "total_votes = 0\n",
    "list_cand = []\n",
    "votes_percand = {}\n",
    "percentage_votes_percand = 0\n",
    "winning_count = 0\n",
    "winning_candidate = \"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4f344017-8a3d-421f-b143-7fda1840b93c",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(file_to_load) as election_data:\n",
    "    reader = list(csv.reader(election_data))\n",
    "    headers = reader[0]\n",
    "\n",
    "    #calculate total number of votes cast\n",
    "    total_votes = len(reader) - 1 #subtract header row\n",
    "\n",
    "    line2 = f\"Total Votes: {total_votes}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fff41639-1495-4dd8-9ba8-97895c69f08f",
   "metadata": {},
   "outputs": [],
   "source": [
    "    #find complete list of candidates who recieved votes\n",
    "    for row in reader[1:]:\n",
    "        candidate = row[2]\n",
    "\n",
    "        if candidate not in list_cand:\n",
    "            list_cand.append(candidate)\n",
    "            votes_percand[candidate] = 0\n",
    "        \n",
    "        votes_percand[candidate] = votes_percand[candidate] + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5b3eddd9-4153-448d-8521-319b21a849d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "    #calculate votes, percentage of votes, and print out winning candidate\n",
    "total_lines = []\n",
    "    for candidate in votes_percand:\n",
    "        votes = votes_percand.get(candidate)\n",
    "        percentage_votes_percand = (float(votes) / float(total_votes))*100\n",
    "        line3 = f\"{candidate}: {percentage_votes_percand:.3f}% ({votes})\\n\"\n",
    "        total_lines.append(line3)\n",
    "        \n",
    "        if (votes > winning_count):\n",
    "            winning_count = votes\n",
    "            winning_candidate = candidate\n",
    "            \n",
    "line4 = f\"Winner: {winning_candidate}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a09c819c-65ed-4b9b-bd12-5f7c10cc6320",
   "metadata": {},
   "outputs": [],
   "source": [
    "#print out to analysis.txt\n",
    "title = \"Election Results\"\n",
    "dash_line = '-' * 30\n",
    "\n",
    "lines = [\n",
    "    title,\n",
    "    dash_line,\n",
    "    line2,\n",
    "    dash_line,\n",
    "    \"\".join(total_lines),\n",
    "    dash_line,\n",
    "    line4,\n",
    "    dash_line\n",
    "]\n",
    "\n",
    "with open('analysis/election_analysis', 'w') as file:\n",
    "    for line in lines:\n",
    "        file.write(line + '\\n')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
