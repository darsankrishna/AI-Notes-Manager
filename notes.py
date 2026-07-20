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