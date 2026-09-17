# Write a program to find the maximum sum of a contiguous subarray.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = arr[0]
maximum = arr[0]

start = 0
end = 0
temp = 0

for i in range(1, len(arr)):
    if arr[i] > current + arr[i]:
        current = arr[i]
        temp = i
    else:
        current = current + arr[i]

    if current > maximum:
        maximum = current
        start = temp
        end = i

print("Maximum Subarray Sum:", maximum)
print("Subarray:", arr[start:end + 1])