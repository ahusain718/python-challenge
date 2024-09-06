{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d37b282f-5187-4168-a45a-77ba586ca7bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os\n",
    "\n",
    "#establish connection to files\n",
    "file_to_load = os.path.join(\"resources\", \"budget_data.csv\")\n",
    "file_to_output = os.path.join(\"python-challenge\", \"PyBank\", \"analysis\", \"budget_analysis\")\n",
    "\n",
    "#initialize variables\n",
    "total_months = 0\n",
    "total_net = 0\n",
    "total_change = 0\n",
    "average_change = 0\n",
    "greatest_inc = 0\n",
    "greatest_dec = 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7ae8c419-0c9b-443e-b92f-8d1129799c0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(file_to_load) as financial_data:\n",
    "    reader = list(csv.reader(financial_data))\n",
    "\n",
    "    # Calculate total months\n",
    "    for i in range(0, len(reader) - 1): \n",
    "        row = reader[i]\n",
    "        next_row = reader[i + 1]\n",
    "\n",
    "        if row != next_row:\n",
    "                total_months += 1\n",
    "\n",
    "    line1 = f\"Total Months: {total_months}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e8d7a716-8352-4f02-8340-c71c57d44e19",
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Calculate net total profit/loss\n",
    "    headers = reader[0]\n",
    "    col_index = headers.index('Profit/Losses')\n",
    "    column_data = [float(row[col_index]) \n",
    "        for row in reader[1:] if row[col_index]] \n",
    "\n",
    "    total_net = round(sum(column_data))\n",
    "\n",
    "    line2 = f\"Total: ${total_net}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "024fdff8-8dcc-424a-ac8c-49bd93337b45",
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Calculate the average change in Profit/Losses over the period\n",
    "    for i in range(len(column_data) - 1):\n",
    "        change = column_data[i + 1] - column_data[i]\n",
    "        total_change += change\n",
    "        average_change = total_change / (len(column_data) - 1)\n",
    "       \n",
    "    line3 = f\"Average Change: ${average_change:.2f}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "78a7c47e-7e8b-454b-92c7-ef40cfa340b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "        headers = reader[0]\n",
    "        col_date = headers.index('Date')\n",
    "        date_data = [row[col_date] for row in reader[1:]]\n",
    "\n",
    "        # Calculate greatest inc and dec in profits\n",
    "        changes = [column_data[i + 1] - column_data[i] for i in range(len(column_data) - 1)]\n",
    "        greatest_inc = round(max(changes))\n",
    "        index_of_greatest_inc = changes.index(greatest_inc)\n",
    "\n",
    "        date_for_greatest_inc = date_data[index_of_greatest_inc + 1]\n",
    "            \n",
    "        line4 = f\"Greatest Increase in Profits: {date_for_greatest_inc} (${greatest_inc})\"\n",
    "\n",
    "        greatest_dec = round(min(changes))\n",
    "        index_of_greatest_dec = changes.index(greatest_dec)\n",
    "\n",
    "        date_for_greatest_dec = date_data[index_of_greatest_dec + 1]\n",
    "            \n",
    "        line5 = f\"Greatest Decrease in Profits: {date_for_greatest_dec} (${greatest_dec})\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "096858f8-beb4-40fa-83b5-959f6764a415",
   "metadata": {},
   "outputs": [],
   "source": [
    "#print to analysis.txt\n",
    "title = \"Financial Analysis\"\n",
    "dash_line = '-' * 30\n",
    "\n",
    "lines = [\n",
    "    title,\n",
    "    dash_line,\n",
    "    line1,\n",
    "    line2,\n",
    "    line3,\n",
    "    line4,\n",
    "    line5\n",
    "]\n",
    "\n",
    "with open('analysis/budget_analysis', 'w') as file:\n",
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
