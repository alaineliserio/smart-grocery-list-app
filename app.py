# Smart Grocery List App (Terminal Version)

grocery_list = []

def add_item():
    item = input("Enter item to add: ").strip()

    if item == "":
        print("Error: item cannot be empty")
        return

    grocery_list.append(item)
    print(f"'{item}' added successfully.")

def remove_item():
    item = input("Enter item to remove: ").strip()

    if item in grocery_list:
        grocery_list.remove(item)
        print(f"'{item}' removed successfully.")
    else:
        print("Error: item not found.")

def view_list():
    print("\n--- Grocery List ---")

    if len(grocery_list) == 0:
        print("List is empty.")
    else:
        for i, item in enumerate(grocery_list, start=1):
            print(f"{i}. {item}")

def main():
    while True:
        print("\n=== Smart Grocery List App ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()