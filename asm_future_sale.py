import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('C:/Users/DELL/OneDrive/Documents/Notepad/product_detail_table.csv')
df_old = df[df['Price'] > 0]
df_new = df[df['Price'] == 0]
X_old = df_old[['Cost', 'StockQuantity', 'ProductGroupID', 'SupplierID']]
y_old = df_old['Price']
X_new = df_new[['Cost', 'StockQuantity', 'ProductGroupID', 'SupplierID']]
X_train, X_test, y_train, y_test = train_test_split(X_old, y_old, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
future_sales_predictions = model.predict(X_new)

df_new['Price'] = future_sales_predictions
df_combined = pd.concat([df_old, df_new], ignore_index=True)
df_combined.to_csv('product_detail_with_predictions.csv', index=False)

print("Dự đoán doanh số bán hàng cho dữ liệu mới:")
print(df_new[['ProductID', 'Price']])
