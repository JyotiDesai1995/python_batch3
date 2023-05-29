list1=[12,56,3,4,6,6,8]
print("original list", str(list1))
res=[]
for x in list1:
    if x not in res:
        res.append(x)

print("after removing the duplicates", str(res))
