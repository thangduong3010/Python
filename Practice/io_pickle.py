import pickle

# The name of the file used to store objects
shoplistfile = 'F:\\Github\\Python\\Practice\\Files\\data\\shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# Dumps the object to the file
pickle.dump(shoplist, f)
f.close()

# Destroys the shoplist
del shoplist

# Read back from file
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)