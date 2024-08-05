import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/DELL/OneDrive/Documents/Notepad/customer_table.csv')

print(df.head())

state_counts = df['State'].value_counts()

plt.figure(figsize=(10, 6))
plt.fill_between(state_counts.index, state_counts.values, color="skyblue", alpha=0.4)
plt.plot(state_counts.index, state_counts.values, color="Slateblue", alpha=0.6, linewidth=2)
plt.title('Số lượng khách hàng theo các bang (Biểu đồ diện tích)')
plt.xlabel('Bang')
plt.ylabel('Số lượng khách hàng')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()