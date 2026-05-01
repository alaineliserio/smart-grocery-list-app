# Smart Grocery List App (Prototype)

## Description

This is a simple terminal-based grocery list application developed as a prototype. The app allows users to manage a grocery list by adding, removing, and viewing items. It demonstrates core functionality and basic error handling as part of a minimum viable product (MVP).

## Features

* Add items to the grocery list
* Remove items from the list
* View all items in the list
* Error handling for:

  * Empty input when adding items
  * Removing items that do not exist
  * Invalid menu selections

## How to Run

1. Make sure Python is installed on your computer
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run the program using:
   python grocery_list.py

## Use Cases

1. **Add Item**

   * User inputs an item name
   * Item is added to the grocery list

2. **Remove Item**

   * User inputs an item name
   * Item is removed if it exists
   * Error shown if item is not found

3. **View List**

   * Displays all items in numbered format
   * Shows message if list is empty

## Error Handling

* Prevents adding empty items
* Notifies user if attempting to remove a non-existent item
* Handles invalid menu input with a retry message

## Technologies Used

* Python (standard library only)
* Terminal/Command Line Interface (CLI)


## Notes

This application is a basic prototype and does not store data permanently. All items are lost when the program exits. Future improvements could include saving data to a file and adding a graphical user interface.
