from inventory_utils import load_items, view_items, search_item, add_item, update_item, delete_item

items = load_items()

while True:
    print("\nInventory Manager")
    print("1. View Items")
    print("2. Search Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Add Item")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_items(items)

    elif choice == "2":
        search_item(items)

    elif choice == "3":
        update_item(items)

    elif choice == "4":
        delete_item(items)

    elif choice == "5":
        add_item(items)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
