a = [10, 20, 30, 20, 40 ,50, 60, 40, 30]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
