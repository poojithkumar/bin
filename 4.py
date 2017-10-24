
import pandas as pd
from pandas import Series, DataFrame
titanic_df = pd.read_csv("train.csv")
print("======data headers=======")
print(titanic_df.head())

print("======data descriptioon=======")
titanic_df.drop(["Pclass"],axis=1,inplace=True)
titanic_df.info()
titanic_df.describe()
titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")
print(titanic_df["Embarked"]) 

