"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = dict()
    for i in items:
        if i not in inventory:
            inventory[i] = 1
        elif i in inventory:
            inventory[i] += 1

    return inventory
    

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    for i in items:
        inventory.setdefault(i,0)
        inventory[i] += 1
        
    return inventory
        


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for i in items:
        if i not in inventory:
            continue
        
        if inventory[i] > 0:
            inventory[i] -= 1
         
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    elif item not in inventory:
        return inventory
    return inventory
        

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    result = []
    for key, value in inventory.items():
        if value != 0:
            result.append((key, value))
        elif value == 0:
            continue

    return result
        
            
