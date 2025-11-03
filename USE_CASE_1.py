
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Open': [135, 136, 137, 138, 139, 140, 141, 142],
    'High': [137, 138, 139, 140, 141, 142, 143, 144],
    'Low': [134, 135, 136, 137, 138, 139, 140, 141],
    'Close': [136, 137, 138, 139, 140, 141, 142, 143]
}
df = pd.DataFrame(data)

X = df[['Open', 'High', 'Low']]
y = df['Close']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R² Score:", r2)


plt.plot(y_test.values, label='Actual Prices', marker='o')
plt.plot(y_pred, label='Predicted Prices', marker='x')
plt.title("Stock Market Prediction using Linear Regression")
plt.xlabel("Data Points")
plt.ylabel("Stock Close Price")
plt.legend()
plt.show()
