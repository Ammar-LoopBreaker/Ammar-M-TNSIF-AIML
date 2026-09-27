import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [22, 2, 500],
    [25, 5, 600],
    [30, 1, 800],
    [35, 8, 550],
    [40, 10, 500],
    [28, 3, 900],
    [45, 12, 650],
    [32, 2, 850]
])

y = np.array([1, 0, 1, 0, 0, 1, 0, 1])

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X, y)

age = 30
tenure = 2
monthly_bill = 750

customer = np.array([[age, tenure, monthly_bill]])

prediction = model.predict(customer)

print("Age:", age)
print("Tenure:", tenure)
print("Monthly Bill:", monthly_bill)

if prediction[0] == 1:
    print("Churn Prediction: Leave")
else:
    print("Churn Prediction: Stay")