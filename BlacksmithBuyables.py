# 1. Organize your data into a master dictionary
store_inventory = {
    "Headgear": ["Straw Hat", "Leather Cap", "Iron Helmet", "Steel Helmet", "Copper Helmet"],
    "Facegear": ["Sheisty", "Sock", "Bandana", "COVID Mask", "Goggles"],
    "Undershirt": ["Tank Top", "Thermal Shirt", "Extra Chest Hairs", "Basic Crewneck", "Nothing"],
    "Overshirt": ["Chain Mail", "Nylon Jacket", "Leather Jacket", "Leather T-Shirt", "Nothing"],
    "Belt": ["Leather Belt", "Rope", "Overall Clips", "WWE Belt", "Nothing"],
    "Pants": ["Shorts", "Levis", "Nylon Pants", "Leather Pants", "Nothing"],
    "Shoes": ["Cowboy Boots", "Tennis Shoes", "Flip Flops", "Barefoot Shoes", "Barefoot"],
    "Swords": ["Arming Sword", "Katana", "Wooden Stick (Stiff)", "Rapier", "Nothing"],
    "Shields": ["Round Shield", "Kite Shield", "Heater Shield", "Swat Shield", "Nothing"],
    "Guns": ["Black Powder Gun", "K98", "AA12", "Straw and Spit Balls", "Nothing"]
}

player_inventory = []

def shop():
    print("--- Welcome to Davey's shop ---")

    # Show categories
    categories = list(store_inventory.keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    # Select Category
    choice = int(input("\nSelect a category number to browse: ")) - 1
    category_name = categories[choice]
    items = store_inventory[category_name]

    # Show Items
    print(f"\n--- {category_name} Section ---")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

    # Purchase
    item_choice = int(input(f"Select an item to buy: ")) - 1
    purchased_item = items[item_choice]

    player_inventory.append(purchased_item)
    print(f"\nSuccess! You bought: {purchased_item}")

