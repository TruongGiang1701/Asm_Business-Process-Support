import pandas as pd

df = pd.read_csv('C:/Users/DELL/OneDrive/Documents/Notepad/customer_table.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)

print("Số lượng dữ liệu trống trong mỗi cột:")
print(df.isnull().sum())



