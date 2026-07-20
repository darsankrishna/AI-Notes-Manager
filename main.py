from notes import add_note, view_notes


def main():
    while True:
        print("\n====== AI Notes Manager ======")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()