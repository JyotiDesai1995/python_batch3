list_a = [5, 5, 17, 3, 4, 32, -3]
for i in range(len(list_a)):
    for j in range(i+1, len(list_a)):
        if list_a[i] > list_a[j]:
            list_a[i], list_a[j] = list_a[j], list_a[i]
        
print("Sorted list:", list_a)

