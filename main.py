import pandas as pd
import numpy as np

data = pd.read_csv("Data.csv")
data = data.drop(columns=["Date","Comment","Extra"])
data = data.fillna(0)

diabetic_before_data = (data.loc[:,data.columns.str.contains("Before",case=False)] > 126 ).sum(axis=1)        # As True Means 1. Sums of Trues = Total number of Trues
diabetic_after_data = (data.loc[:,data.columns.str.contains("after",case=False)] > 200 ).sum(axis=1)

diabetic_row_datas = diabetic_before_data + diabetic_after_data

diabetic = diabetic_row_datas >=3


prediabetic_before_data = (data.loc[:,data.columns.str.contains("Before",case=False)] > 99 ).sum(axis=1)        # As True Means 1. Sums of Trues = Total number of Trues
prediabetic_after_data = (data.loc[:,data.columns.str.contains("after",case=False)] > 140 ).sum(axis=1)

prediabetic_row_datas = prediabetic_before_data + prediabetic_after_data

prediabetic = prediabetic_row_datas >=3

conditions=[
    diabetic,
    prediabetic
]

choices=[
    "Diabetic",
    "Prediabetic"
]

data["Status"] = np.select(conditions,choices,default="Normal")

print(data)