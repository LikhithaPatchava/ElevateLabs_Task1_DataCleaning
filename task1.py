import pandas as pd

df = pd.read_csv("data/netflix_titles.csv")

print("Dataset Loaded Successfully")

print(df.isnull().sum())

df = df.drop_duplicates()

df.to_csv("cleaned_netflix_titles.csv", index=False)

print("Data cleaning completed successfully!")