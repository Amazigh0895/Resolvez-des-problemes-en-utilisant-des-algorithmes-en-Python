import pandas as pd
import numpy as np


filePath = "dataCsv/dataset1_Python+P7.csv"
K = 500


# Python3 program to find Closest sum in a list
def closestSum(lst, K):
    lst = np.asarray(lst)
    idx = (np.abs(lst - K)).argmin()
    return lst[idx]


# Python3 program to find Closest index in a list
def closestIndex(lst, K):
    lst = np.asarray(lst)
    idx = (np.abs(lst - K)).argmin()
    return idx


# Read CSV file
data = pd.read_csv(filePath)

# Sort data by profit
dataSortedByProfit = data.sort_values(by="profit", ascending=False)

# Sort by sum  of price
sum = dataSortedByProfit['price'].cumsum()

# Get the closet cost of the actions
closestSumValue = closestSum(sum, K)

# Get the max index
closestIndexValue = closestIndex(sum, K)

# Interessting list of best profits
headInteresstinListProfil = dataSortedByProfit.head(closestIndexValue)

# Get the sum of list profits
profit = (headInteresstinListProfil['profit'].cumsum()).tail(1)

benifitsMaked = profit.iloc[0] - closestSumValue
print(benifitsMaked)
