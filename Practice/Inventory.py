stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    total = 0
    print('Inventory:')

    for i, j in inventory.items():
        print(str(j) + ' ' + i)
        total += j

    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        count = inventory.get(i, 0)
        count += 1

        if i not in inventory:
            inventory.setdefault(i, count)
        else:
            inventory[i] = count

    displayInventory(inventory)


displayInventory(stuff)
print('Adding...')
addToInventory(stuff,dragonloot)