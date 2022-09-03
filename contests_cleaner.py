import pandas as pd

cts = pd.read_csv('contests.csv')

print(cts)

cts = cts.drop_duplicates(keep='first')

print(cts)


