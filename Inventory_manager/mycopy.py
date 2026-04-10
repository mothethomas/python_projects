items = [
    {"Name":"Rice","Quantity":10,"Price":25},
    {"Name":"Soap","Quantity":10, "Price":5},
    {"Name":"Notebook","Quantity":15,"Price":8}
]
def view_items(item_list):
    print("---VIEW items----")
    total_price=0
    grand_total=0
    for x in item_list:
        total_price=x["Quantity"]*x["Price"]
        grand_total += total_price 
        print("Name:",x["Name"],"\nQuantity: ", x["Quantity"],"\nPrice:", x["Price"],"\nTotal Price:",total_price,"\n")
        print("------------------")
    print("Grand Total Inventory Value:", grand_total)


def search_items(item_list):
    print("---Search items----")
    search_item_name=input("Enter the item name to be search:")
    found = False 
    for x in item_list:
        if search_item_name.lower()==x["Name"].lower():
           print("Name:",x["Name"],"\nQuantity: ", x["Quantity"],"\nPrice:", x["Price"])##,"\nTotal Price:",total_price,"\n")
           found=True
           break
    if not found:
            print("Item not found")
 

def add_item(item_list):
     print("---Adding items----")
     add_item_name=input("Enter the name of item\n").capitalize()
   
     if not add_item_name:
        print("Item name cannot be empty.")
        return

     try:
        add_quantity = int(input("Enter the quantity\n"))
        add_price = int(input("Enter the price of item\n"))
     except ValueError:
        print("Please enter valid numbers.")
        return

     if add_quantity < 0 or add_price < 0:
        print("Value should not be negative")
        return   
    

     
     new_list={"Name":add_item_name,"Quantity":add_quantity,"Price":add_price}
     item_list.append(new_list)
     price_sum=add_price*add_quantity
     print("Name:",new_list["Name"],"\nQuantity: ", new_list["Quantity"],"\nPrice:", new_list["Price"],"\nTotal price",price_sum)

def update_item(item_list):
    print("---update quantity and price in items----")
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

            print("Item updated successfully.")
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price:", item["price"])
            print()
            break

    if not found:
        print("Item not found.")
        print()

"""
def update_quantity(item_list):
    print("---update quantity in items----")
    update_quantity_name=input("Enter the item name to be update\n")
    found=False
    for x in item_list:
          if update_quantity_name.lower()==x["Name"].lower():
               found=True
               new_quantity=int(input("Enter the new quantity of the items\n"))
               if not new_quantity:
                   print("Quantity should not be empty.")
                   return           
          if new_quantity < 0:
             print("Value should not be negative")
             return         
        
          print("New quantity of item is", new_quantity)
          x["Quantity"]=new_quantity
          price_sum=x["Quantity"]*x["Price"]
          print("Name:",x["Name"],"\nQuantity:",x["Quantity"],"\nPrice:",x["Price"],"\nTotal Price:",price_sum)
          break
    if not found:
        print("Item not found")
"""

def delete_items(item_list):
     print("---delete items----")
     delete_name=input("Enter the name of item to be deleted:")
     found=False
     for x in item_list:
          if delete_name.lower()==x["Name"].lower():
               found=True
               item_list.remove(x)
               print("Item removed successfully")
               return
     print("item not found")      

    

while True:
    print("\nInventory Manager")
    print("1. View Items")
    print("2. Search Item")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Add Item")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_items(items)

    elif choice == "2":
        search_items(items)

    elif choice == "3":
        update_item(items)

    elif choice == "4":
        delete_items(items)

    elif choice == "5":
        add_item(items)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")