import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([100000, 200000, 300000, 400000, 500000])

model = LinearRegression()
model.fit(X, y)

new_size = np.array([[1800]])
predicted_price = model.predict(new_size)

print("Predicted Price:", predicted_price[0])