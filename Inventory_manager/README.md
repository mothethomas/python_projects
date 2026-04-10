# Inventory Manager

A beginner-friendly Python project to manage inventory items using lists, dictionaries, functions, JSON file handling, and a menu-driven program.

## What this project does

This project helps manage inventory data from the terminal.

You can:
- view all items
- search for an item
- add a new item
- update item quantity and price
- delete an item
- store data in a JSON file
- load saved data when the program starts

## Features

- Menu-driven Python program
- Item data stored as dictionaries inside a list
- Search item by name
- Add new item
- Update item quantity and price
- Delete an item
- View total value of each item
- Case-insensitive item search
- Validation for empty names
- Validation for invalid quantity and price
- Exception handling for non-numeric input
- Data persistence using `items.json`
- Code split into multiple files:
  - `main.py`
  - `inventory_utils.py`

## Project Structure

```bash
inventory_manager/
│
├── main.py
├── inventory_utils.py
├── items.json
└── README.md