import seaborn as sns
import pandas as pd
import numpy as np

sns.set()

df = pd.read_csv("hr_data.csv")

# print(df.select_dtypes(exclude=["int", "float"]).columns)

# print(df["department"].unique())
# print(df["salary"].unique())

emp_satis = pd.read_excel("employee_satisfaction_evaluation.xlsx")

# print(emp_satis.head())

main_df = df.set_index("employee_id").join(emp_satis.set_index("EMPLOYEE #"))
main_df = main_df.reset_index()
# print(main_df.head())

# print(main_df[main_df.isnull().any(axis=1)])

# main_df.fillna(main_df.mean(), inplace=True)
# print(main_df)
# print(main_df.describe())

main_df_final = main_df.drop(columns="employee_id")
# print(main_df.groupby("department").sum())
# print(main_df.groupby("department").mean())

import matplotlib.pyplot as plt


def plot_corr(df):
    plt.figure(figsize=(12, 9))
    s = sns.heatmap(df.corr(), annot=True, cmap='RdBu', vmin=-1, vmax=1)
    s.set_yticklabels(s.get_yticklabels(), rotation=0, fontsize=12)
    s.set_xticklabels(s.get_xticklabels(), rotation=90, fontsize=12)
    plt.title('Corr Heat Map')
    plt.show()


plot_corr(main_df_final)
