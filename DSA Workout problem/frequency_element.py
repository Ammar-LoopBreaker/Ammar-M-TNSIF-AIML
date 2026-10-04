# Write a program to find the element that occurs the maximum number of times in an array.

arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

max_count = 0
most_frequent = 0

for num in arr:
    count = 0

    for x in arr:
        if num == x:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = num

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_count)