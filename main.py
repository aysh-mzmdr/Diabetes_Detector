import pandas as pd

data = pd.read_csv("Data.csv")
data = data.drop(columns=["Date","Comment","Extra"])
data = data.fillna(0)

before_data = (data.loc[:,data.columns.str.contains("Before",case=False)] > 99 ).sum(axis=1)        # As True Means 1. Sums of Trues = Total number of Trues
after_data = (data.loc[:,data.columns.str.contains("after",case=False)] > 140 ).sum(axis=1)

row_datas = before_data + after_data

data["Status"] = row_datas >=3 

print(data)