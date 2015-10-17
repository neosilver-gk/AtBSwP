
def display_inv(inventory):

    print('Invertory: ')
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        item_total += value
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, lootlist):

    for lootItem in lootlist:
        inventory.setdefault(lootItem, 0)
        inventory[lootItem] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'rudy']
inv = addToInventory(inv, dragonLoot)
display_inv(inv)
