import json


def load_items():
    try:
        with open("items.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"name": "Rice", "quantity": 10, "price": 25},
            {"name": "Soap", "quantity": 20, "price": 5},
            {"name": "Notebook", "quantity": 15, "price": 8}
        ]


def save_items(item_list):
    with open("items.json", "w") as file:
        json.dump(item_list, file, indent=4)





def view_items(item_list):
    if not item_list:
        print("No items available.")
        print()
        return

    for item in item_list:
        print("Name:", item["name"])
        print("Quantity:", item["quantity"])
        print("Price:", item["price"])
        total_value = item["quantity"] * item["price"]
        print("Total Value:", total_value)
        print()


def search_item(item_list):
    search_name = input("Enter item name to search: ")

    if not search_name.strip():
        print("Item name cannot be empty.")
        return

    found = False

    for item in item_list:
        if search_name.lower() == item["name"].lower():
            found = True
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price:", item["price"])
            total_value = item["quantity"] * item["price"]
            print("Total Value:", total_value)
            print()
            break

    if not found:
        print("Item not found.")
        print()


def add_item(item_list):
    item_name = input("Enter the name of the item: ")

    if not item_name.strip():
        print("Item name cannot be empty.")
        return

    found = False

    for item in item_list:
        if item_name.lower() == item["name"].lower():
            found = True
            break

    if found:
        print("Item already exists.")
    else:
        try:
            quantity = int(input("Enter the quantity of the item: "))
            price = int(input("Enter the price of the item: "))
        except ValueError:
            print("Please enter only numbers for quantity and price.")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if price <= 0:
            print("Price must be greater than 0.")
            return

        new_item = {
            "name": item_name,
            "quantity": quantity,
            "price": price
        }

        item_list.append(new_item)
        save_items(item_list)
        print("Item added successfully.")
        print()


def update_item(item_list):
    update_name = input("Enter the item name to update: ")

    if not update_name.strip():
        print("Item name cannot be empty.")
        return

    found = False

    for item in item_list:
        if update_name.lower() == item["name"].lower():
            found = True

            try:
                new_quantity = int(input("Enter the new quantity: "))
                new_price = int(input("Enter the new price: "))
            except ValueError:
                print("Please enter only numbers for quantity and price.")
                return

            if new_quantity < 0:
                print("Quantity cannot be negative.")
                return

            if new_price <= 0:
                print("Price must be greater than 0.")
                return

            item["quantity"] = new_quantity
            item["price"] = new_price
            save_items(item_list)

            print("Item updated successfully.")
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price:", item["price"])
            print()
            break

    if not found:
        print("Item not found.")
        print()


def delete_item(item_list):
    delete_name = input("Enter item name to delete: ")

    if not delete_name.strip():
        print("Item name cannot be empty.")
        return

    found = False

    for item in item_list:
        if delete_name.lower() == item["name"].lower():
            found = True
            item_list.remove(item)
            save_items(item_list)
            print("Item deleted successfully.")
            print()
            break

    if not found:
        print("Item not found.")
        print()

