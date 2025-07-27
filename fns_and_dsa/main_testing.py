from shopping_list_manager import add_item, remove_item, display_list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
            pass
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
            pass
        elif choice == '3':
            # Display the shopping list
            items = display_list()
            print("Shopping List:")
            for i in items:
                print(f"- {i}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()