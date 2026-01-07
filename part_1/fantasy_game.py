loot = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12,
    'dagger': 3
}

def display_inventory(items: dict) -> None:
    print("\nInventory:\n")
    inv = {}
    total = 0
    for item, quantity in items.items():
        if item not in inv.keys():
            inv.setdefault(item, quantity)
            total += quantity
        else:
            inv[item] += quantity
            total += quantity

    for item, quantity in inv.items():
        print("{} {}".format(quantity, item))
    
    print("\nTotal items: {}".format(total))


display_inventory(loot)