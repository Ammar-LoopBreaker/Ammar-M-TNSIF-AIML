import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]
sales = [25000, 30000, 28000, 35000, 40000, 38000]

plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

plt.show()

plt.bar(months, sales, label="Monthly Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

plt.show()