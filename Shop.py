from BlacksmithBuyables import store_inventory
from SaveManager import auto_save


def shop(player, story):
    while True:
        print("\n--- Welcome to Davey's Shop ---")

        categories = list(store_inventory.keys())

        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        print("0. Leave Shop")

        choice = input("\nChoose a category: ").strip()

        if choice == "0":
            print("Davey: Safe travels, friend.")
            return

        if not choice.isdigit() or not (1 <= int(choice) <= len(categories)):
            print("Invalid choice.")
            continue

        category_name = categories[int(choice) - 1]
        browse_category(player, story, category_name)


def browse_category(player, story, category_name):
    items = store_inventory[category_name]

    while True:
        print(f"\n--- {category_name} ---")

        for i, item in enumerate(items, 1):
            print(f"{i}. {item['name']} - {item['price']} gold "
                  f"(ATK {item['atk']} / DEF {item['def']} / HP {item['hp']})")

        print("0. Back to Categories")

        choice = input("\nChoose an item to buy: ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not (1 <= int(choice) <= len(items)):
            print("Invalid choice.")
            continue

        purchase_item(player, story, items[int(choice) - 1])


def purchase_item(player, story, item):
    if player.gold < item["price"]:
        print("You don't have enough gold!")
        return

    player.gold -= item["price"]
    player.inventory.add_item(item)
    print(f"You bought: {item['name']}!")
    auto_save(player, story)
