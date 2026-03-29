import pandas as pd

data = pd.read_csv("Data.csv")
data = data.drop(columns=["Date","Comment","Extra"])
data = data.fillna(0)

data["Status"] = (data.loc[:,data.columns.str.contains("Before",case=False)] > 99 ).any(axis=1)
data["Status"] = data["Status"] | (data.loc[:,data.columns.str.contains("after",case=False)] > 140 ).any(axis=1)

print(data)