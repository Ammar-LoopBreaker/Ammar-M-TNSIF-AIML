import pandas as pd

data = {
    "Product Name": ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Tablet"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 25000, 2000, 1500, 800, 30000],
    "Quantity Sold": [30, 70, 100, 60, 80, 40]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Sales Data:")
print(df)

print("\nProduct with Highest Sales:")
print(df.loc[df["Total Sales"].idxmax()])

print("\nAverage Product Price:", df["Price"].mean())

print("\nProducts with Quantity Sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

print("\nProducts Sorted by Total Sales:")
print(df.sort_values("Total Sales", ascending=False))