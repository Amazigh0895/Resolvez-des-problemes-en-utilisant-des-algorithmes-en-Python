import csv
import itertools



filePath = "dataCsv/dataTest.csv"
max_budget = 500
NULL_NUMBER = 0.0


# sort function
def sort_data(data, max_budget):
    best_combination = []
    best_profit = []
    best_profit = 0.0
    total_cost = 0.0
    total = 0.0
    best = 0.0

    for r in range(1, len(data) + 1):
        combinations = itertools.combinations(data, r)
        for combination in combinations:
            total_cost = sum(float(item[0]) for item in combination)
            if total_cost <= max_budget:
                total_profit = sum(float(item[1]) for item in combination)
                if total_profit > best_profit:
                    best_combination.append(combination)
                    best_profit = total_profit
    
    best_combination = best_combination[len(best_combination)-1]
    # Print list of best combination investment
    for combination in best_combination:
        print(combination)
        total += float(combination[0])
        best += float(combination[1])
    print("---------------------------")
    print(" La somme des coùt est de ", total, " euros ")
    print(" Le benifice tiré est de ", best, " euros")


# Loading data from csv file
def chargingData():
    with open(filePath, newline="") as file:
        reader = csv.reader(file, delimiter=',')
        rows = []
        for row in reader:
            if row[0] == "name" or int(row[0]) <= NULL_NUMBER or int(row[1]) <= NULL_NUMBER:
                pass
            else:
                row[1] = float(row[0]) * float(row[1]) / 100
                rows.append(row)
    return rows


# Starting programme function
def startProgrammBrute():
    rows = chargingData()
    sort_data(rows, max_budget)