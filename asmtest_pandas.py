import pandas as pd

df = pd.read_csv('C:/Users/DELL/OneDrive/Documents/Notepad/customer_table.csv')


# Kiểm tra số lượng dữ liệu trống trong cột LastName trước khi điền
print("Số lượng dữ liệu trống trong cột trước khi điền:")
print(df.isnull().sum())

# Thay thế các giá trị chuỗi rỗng bằng NaN
df['LastName'].replace('', pd.NA, inplace=True)

# Điền các giá trị trống bằng 'giang' trong cột LastName
df['LastName'].fillna("dang", inplace=True)

# Kiểm tra lại số lượng dữ liệu trống sau khi điền
print("Số lượng dữ liệu trống trong mỗi cột sau khi điền:")
print(df.isnull().sum())
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)

