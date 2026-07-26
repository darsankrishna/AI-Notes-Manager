notes = []


def add_note():
    note = input("Enter your note: ").strip()

    if note:
        notes.append(note)
        print("Note added successfully!")
    else:
        print("Empty notes are not allowed.")


def view_notes():
    if not notes:
        print("\nNo notes available.")
        return

    print("\nYour Notes:")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")

def delete_note():
    if not notes:
        print("\nNo notes available.")
        return

    print("\nYour Notes:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")

    try:
        choice = int(input("\nEnter note number to delete: "))

        if 1 <= choice <= len(notes):
            deleted_note = notes.pop(choice - 1)
            print(f"\n'{deleted_note}' deleted successfully.")
        else:
            print("\nInvalid note number.")

    except ValueError:
        print("\nPlease enter a valid number.")