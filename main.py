import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1xtOY92SE7SKYJ9CHApFPH6z8q9inZum9bCUJRn6NLHk/export?format=csv'

#trocar o final do link por: "/export?format=csv"

df = pd.read_csv(url)

print(df.head())
