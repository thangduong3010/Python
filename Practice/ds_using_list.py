
shoplist = ["apple", "mango", "carrot", "banana"]

print("I have {} items to purchase".format(len(shoplist)))

print("These items are:"),
for item in shoplist:
    print(item),

print("\nI also have to buy rice")
shoplist.append("rice")
print("My shop list is now: {}".format(shoplist))

print("I will sort my list now")
shoplist.sort()
print("Sort list: {}".format(shoplist))

print("The first item I'll buy is: {}".format(shoplist[0]))
olditem = shoplist[0]
del shoplist[0]
print("I bought the {}".format(olditem))
print("My shop list is now: {}".format(shoplist))
