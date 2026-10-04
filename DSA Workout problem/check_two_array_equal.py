''' Given two arrays, check whether they contain the same elements with the same frequency,
 regardless of their order.'''
 
arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 1, 2, 3]

if sorted(arr1) == sorted(arr2):
    print("Arrays are Equal")
else:
    print("Arrays are Not Equal")