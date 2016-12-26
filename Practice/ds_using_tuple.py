
zoo = ("python", "elephant", "penguin")
print("Number of animals in the zoo: {}".format(len(zoo)) )

new_zoo = "monkey", "camel", zoo
print("Number of cages in the new zoo: {}".format(len(new_zoo)) )
print("All animals in the new zoo: {}".format(new_zoo))
print("Animals bought from the old zoo: {}".format(new_zoo[2]))
print("Last animal bought from the old zoo: {}".format(new_zoo[2][2]))


