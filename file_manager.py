from pathlib import Path


# Display all available options
def show_menu():
    print("\n" + "=" * 40)
    print("      FILE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Show files in current folder")
    print("6. Exit")
    print("=" * 40)


# Create a new file and write initial content
def create_file():
    filename = input("Enter file name: ").strip()
    file_path = Path(filename)

    if file_path.exists():
        print("A file with that name already exists.")
        return

    content = input("Write something for the file: ")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"'{filename}' created successfully.")


# Read and display file content
def read_file():
    filename = input("Enter file name: ").strip()
    file_path = Path(filename)

    if not file_path.exists():
        print("File not found.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print("\n--- File Content ---")
    print(content)
    print("--------------------")


# Update existing files
def update_file():
    filename = input("Enter file name: ").strip()
    file_path = Path(filename)

    if not file_path.exists():
        print("File not found.")
        return

    print("\nWhat would you like to do?")
    print("1. Rename file")
    print("2. Append content")
    print("3. Replace all content")

    option = input("Choose an option: ").strip()

    if option == "1":
        new_name = input("New file name: ").strip()
        new_path = Path(new_name)

        if new_path.exists():
            print("Another file already has that name.")
            return

        file_path.rename(new_path)
        print("File renamed successfully.")

    elif option == "2":
        new_text = input("Enter text to append: ")

        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n" + new_text)

        print("Content added successfully.")

    elif option == "3":
        new_text = input("Enter new content: ")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_text)

        print("File content replaced successfully.")

    else:
        print("Invalid option selected.")


# Delete a file after confirmation
def delete_file():
    filename = input("Enter file name: ").strip()
    file_path = Path(filename)

    if not file_path.exists():
        print("File not found.")
        return

    confirmation = input(
        f"Are you sure you want to delete '{filename}'? (y/n): "
    ).lower()

    if confirmation == "y":
        file_path.unlink()
        print("File deleted.")
    else:
        print("Deletion cancelled.")


# Small utility feature:
# shows files in the current working directory
def list_files():
    files = [item for item in Path(".").iterdir() if item.is_file()]

    if not files:
        print("No files found in this folder.")
        return

    print("\nFiles in current directory:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")


def main():
    while True:
        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            create_file()

        elif choice == "2":
            read_file()

        elif choice == "3":
            update_file()

        elif choice == "4":
            delete_file()

        elif choice == "5":
            list_files()

        elif choice == "6":
            print("Thanks for using the File Management System.")
            break

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()