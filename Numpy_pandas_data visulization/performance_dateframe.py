import pandas as pd

data = {
    "Name": ["Anwar", "Aravidh", "Rahul", "Priya", "Kavin", "Divya", "Vijay", "Anu"],
    "Department": ["CSE", "ECE", "CSE", "IT", "CSE", "ECE", "IT", "CSE"],
    "Marks": [85, 72, 90, 65, 78, 88, 95, 70],
    "Attendance": [90, 75, 85, 92, 78, 88, 95, 72]
}

df = pd.DataFrame(data)

print("First 5 Students:")
print(df.head())

print("\nAverage Marks:", df["Marks"].mean())

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted by Marks:")
print(df.sort_values("Marks"))