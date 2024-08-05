import pandas as pd

df = pd.read_csv('C:/Users/DELL/OneDrive/Documents/Notepad/customer_table.csv')

print("Số lượng dữ liệu trống trong cột trước khi điền:")
print(df.isnull().sum())

df['LastName'].replace('', pd.NA, inplace=True)
df['LastName'].fillna("dang", inplace=True)

print("Số lượng dữ liệu trống trong mỗi cột sau khi điền:")
print(df.isnull().sum())
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)

