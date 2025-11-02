import pandas as pd

try:
    df = pd.read_csv("md.csv", sep=",", quotechar='"', engine="python")
    print("CSV loaded successfully!")
    print(df.head())
except Exception as e:
    print("Error reading CSV:", e)
