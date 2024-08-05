import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('C:/Users/DELL/OneDrive/Documents/Notepad/product_detail_table.csv')
X = df[['Cost', 'StockQuantity', 'ProductGroupID', 'SupplierID']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

Smartphone = pd.DataFrame({
    'Cost': [500],
    'StockQuantity': [100],
    'ProductGroupID': [1],
    'SupplierID': [1]
})
predicted_price = model.predict(Smartphone)
print(f"Predicted Price: {predicted_price[0]}")
