
print("Simple assignment")
shoplist = ["apple", "mango", "carrot", "banana"]

mylist = shoplist
del shoplist[0]

print("Shoplist: {}".format(shoplist))
print("Mylist: {}".format(mylist))

print("Copy by making a full slice")
mylist = shoplist[:]
del mylist[0]

print("Shoplist: {}".format(shoplist))
print("Mylist: {}".format(mylist))