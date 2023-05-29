grocery_list = []
def add_items(*args):
    print(args)
    grocery_list.extend(args)
add_items('apples', 'bananas','sugar')
#('apples', 'bananas', 'sugar') #since we use a print statement in the function
print(grocery_list)
#['apples', 'bananas', 'sugar']
