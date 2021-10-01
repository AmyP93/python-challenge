##Main script to run for each analysis

import csv

budget_data_csv = "C:\\1-SMU DATA VISUA\\1-Github\\Repos\\python-challenge\\PyBank\\Resources\\budget_data.csv"

file_to_output = "PyBank/Analysis/PyBank_analysis.txt"

#variables to track
total_months = 0
total_ProfitLoss = 0
prev_ProfitLoss = 0
ProfitLoss_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 99999999999]

#read csv and create dictionary

with open(budget_data_csv) as ProfitLoss_data:
    csvreader = csv.DictReader(ProfitLoss_data)

    for row in csvreader:

        #Track the totals
        total_months = total_months + 1
        total_ProfitLoss = total_ProfitLoss + int(row["Profit/Losses"])

        #Track the ProfitLoss change

        ProfitLoss_change = int(row["Profit/Losses"]) - prev_ProfitLoss
        prev_ProfitLoss = int(row["Profit/Losses"])
        ProfitLoss_change_list.append(ProfitLoss_change)
        month_change = [row["Date"]]

        #Calculate greatest increase
        if (ProfitLoss_change > greatest_increase[1]):
            greatest_increase [0] = row["Date"]
            greatest_increase[1] = ProfitLoss_change

        #Calculate greatest decrease
        if (ProfitLoss_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = ProfitLoss_change
            
#Calculate the changes in Profit/Losses and find the average
ProfitLoss_change_list.pop(0)

ProfitLoss_avg = sum(ProfitLoss_change_list)/len(ProfitLoss_change_list)

#Create output summary
output = (
    f"\nFinancial Analysis\n"
    f"------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Profit/Loss: ${total_ProfitLoss}\n"
    f"Average Profit/Loss: ${round(ProfitLoss_avg,2)}\n" 
    f"Greatest increase in Profits: {greatest_increase [0]} (${greatest_increase [1]})\n"
    f"Greatest decrease in Profits: {greatest_decrease [0]} (${greatest_decrease [1]})\n"
)

#Print the output to VSC
print(output)

#Create text file in Analysis folder

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


#how can I add "{:.2f}" for two decimal places on greatest increase/decrease?


















        






