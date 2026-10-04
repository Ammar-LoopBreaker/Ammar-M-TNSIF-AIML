import matplotlib.pyplot as plt

students = ["Anwar", "Aravindh", "Rahul", "Priya", "Kavin", "Divya", "Vijay", "Anu", "Ravi", "Meena"]
marks = [85, 72, 95, 68, 55, 88, 35, 45, 78, 25]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

excellent = 0
good = 0
average = 0
needs_improvement = 0

for mark in marks:
    if mark >= 80:
        excellent += 1
    elif mark >= 60:
        good += 1
    elif mark >= 40:
        average += 1
    else:
        needs_improvement += 1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
counts = [excellent, good, average, needs_improvement]

plt.pie(counts, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")

plt.show()