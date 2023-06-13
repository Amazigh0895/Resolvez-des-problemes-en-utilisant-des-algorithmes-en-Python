import csv
import math

filePath = "dataCsv/dataset2_Python+P7.csv"
max_budget = 500
NULL_NUMBER = 0.0


# Loading data from csv file
def chargingData():
    with open(filePath, newline="") as file:
        reader = csv.reader(file, delimiter=',')
        rows = [] 
        for row in reader:
            if row[0] == "name" or float(row[1]) <= NULL_NUMBER or float(row[2]) <= NULL_NUMBER:
                pass
            else:
                # Get benifice
                benifice = float(row[1]) * float(row[2]) / 100
                # Get rendment 
                rendement = math.floor(max_budget/float(row[1])) * float(row[1]) * (1+ float(row[2]) / 100)  - math.floor(max_budget/float(row[1])) * float(row[1])
                row.append(benifice)
                row.append(rendement)
                rows.append(row)
    return rows


# Sort function
def sort_data(data, max_budget):
    n = len(data)
    total_profit, total_cost, i, bestListProfit = 0.0, 0.0, 0, []
    while max_budget > 1:
        if max_budget >= float(data[i][1]) and i < n-1:
            total_cost += float(data[i][1])
            total_profit += float(data[i][3])
            price = data[i][1]
            #profit = data[i][3]
            #bestListProfit.append(name)
            bestListProfit.append(price)
            #bestListProfit.append(profit)
            max_budget -= float(data[i][1])
            i = i+1
        else:
            while max_budget < float(data[i][1]) and i < n-1:
                i = i + 1
    print("---------------------------")
    print(" La somme des coùt est de ", total_cost, " euros ")
    print(" Le benifice tiré est de ", total_profit, " euros")
    for profit in bestListProfit:
        print(profit)


# Start function
def startProgrammOptimized():
    """starting programm"""

    rows = chargingData()
    # Sort data by rendmment
    rows = sorted(rows, key=lambda rows: float(rows[4]), reverse=True)

    sort_data(rows, max_budget)
