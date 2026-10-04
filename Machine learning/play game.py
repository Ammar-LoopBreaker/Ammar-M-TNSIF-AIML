import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

data = {
    "Weather": ["Sunny", "Sunny", "Rainy", "Rainy", "Cloudy", "Cloudy", "Sunny", "Rainy"],
    "Temperature": ["Hot", "Cool", "Cool", "Hot", "Hot", "Cool", "Hot", "Cool"],
    "Play": [0, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()

df["Weather"] = weather_encoder.fit_transform(df["Weather"])
df["Temperature"] = temperature_encoder.fit_transform(df["Temperature"])

X = df[["Weather", "Temperature"]]
y = df["Play"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

weather = "Sunny"
temperature = "Cool"

weather_value = weather_encoder.transform([weather])[0]
temperature_value = temperature_encoder.transform([temperature])[0]

prediction = model.predict([[weather_value, temperature_value]])

print("Weather:", weather)
print("Temperature:", temperature)

if prediction[0] == 1:
    print("Play Prediction: Yes")
else:
    print("Play Prediction: No")