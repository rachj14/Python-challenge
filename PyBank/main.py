import os
import csv
budget_data = os.path.join('Resources', 'budget_data.csv')

#Set variables
months = []
profit_loss = []
changes = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:

        months.append(row[0])
        profit_loss.append(int(row[1]))

        total_months = len(months)

        net_total = sum(profit_loss)

    for i in range(1, total_months):
        change = profit_loss[i] - profit_loss[i-1]
        changes.append(change)

        average_change = sum(changes) / len(changes)

    greatest_increase = max(changes)
    greatest_increase_date = months[changes.index(greatest_increase) + 1]
    greatest_decrease = min(changes)
    greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    




