import pandas as pd
import os

folder_path = 'scraped vahan'
excel_files = [file for file in os.listdir(
    folder_path) if file.endswith('.xlsx')]

dfs = []

for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    dfs.append(df)


# title = dfs.columns[0]
# dfs.columns = range(dfs.shape[1])
# dfs['RTO'] = title
# dfs = dfs.iloc[2:]
# combined_df = pd.concat(dfs, ignore_index=True)
# dfs.to_csv('data.csv')
