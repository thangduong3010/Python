
ab = {
    "Swaroop": "swaroop@abc.com",
    "Larry": "larry@wall.com",
    "Matsumoto": "matz@ruby.com"
}

print("Swaroop's address: {}".format(ab["Swaroop"]))
print("There are {} contacts in the book\n".format(len(ab)))

for name, address in ab.items():
    print("Contact {} at {}".format(name,address))

for name in ab.keys():
    print("Name: {}".format(name))

for address in ab.values():
    print("Add: {}".format(address))

a = "hello"
print("{}".format(a[:-1]))