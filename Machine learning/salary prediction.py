import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000])

model = LinearRegression()
model.fit(X, y)

experience = np.array([[5]])
predicted_salary = model.predict(experience)

print("Years of Experience:", experience[0][0])
print("Predicted Salary:", predicted_salary[0])