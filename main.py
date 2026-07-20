from notes import add_note


def main():
    while True:
        print("\n====== AI Notes Manager ======")
        print("1. Add Note")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()