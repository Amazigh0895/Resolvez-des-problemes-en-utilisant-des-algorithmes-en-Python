import csv


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
                row[2] = float(row[1]) * float(row[2]) / 100
                rows.append(row)
    return rows


rows = chargingData()
rows = sorted(rows, key=lambda rows: float(rows[2]), reverse=True)

for row in rows:
    print(row)
#print(rows[2][2])
# sort function
def sort_data(data, max_budget):
    
    n = len(data)
    
    #print(n)
    total_profit = 0.0
    total_cost = 0.0
    i = 0

    while max_budget > 0:
        if max_budget >= float(data[i][1]):
            total_cost += float(data[i][1])
            print(total_cost)
            #print(total_profit)
            total_profit += float(data[i][2])
        max_budget -= float(data[i][1])
        i = i+1
        #print(max_budget)
        
    print("---------------------------")
    print(" La somme des coùt est de ", total_cost, " euros ")
    print(" Le benifice tiré est de ", total_profit, " euros")

sort_data(rows,max_budget)