list_a = [5, 5, 17, 3, 4, 32, -30]
new_list = []
while list_a:
    min=list_a[0]
    for no in list_a:
        if no < min:
            min = no
    new_list.append(min)
    list_a.remove(min)
            
    
print("Sorted list:", new_list)

