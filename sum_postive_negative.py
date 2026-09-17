# Write a program to find the separate sum of positive and negative numbers in an array.

arr = [10, -5, 20, -8, 15, -2]

positive = 0
negative = 0

for num in arr:
    if num > 0:
        positive += num
    else:
        negative += num

print("Positive Sum:", positive)
print("Negative Sum:", negative)