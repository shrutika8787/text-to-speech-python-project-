import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv(r"c:\Users\Admin\Documents\project\js\omify\Sheetlist.csv")

print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Sheetlist.html")
