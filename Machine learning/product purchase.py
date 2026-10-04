import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

X = np.array([
    [20, 15000],
    [22, 18000],
    [25, 25000],
    [28, 30000],
    [30, 35000],
    [35, 40000],
    [40, 50000],
    [45, 60000]
])

y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

model.fit(X, y)

age = 32
income = 38000

customer = np.array([[age, income]])

prediction = model.predict(customer)

print("Age:", age)
print("Income:", income)

if prediction[0] == 1:
    print("Purchase Prediction: Yes")
else:
    print("Purchase Prediction: No")