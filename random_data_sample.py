import pandas as pd
df = pd.read_csv("./Carrie_full_crater_db.csv")
new_dataframe = df.sample(200000, frac = None, axis = None, replace = False, ignore_index = False)
print(len(df))


import csv
new_dataframe.to_csv('random_sample.csv',sep = ",")
