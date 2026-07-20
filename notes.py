notes = []


def add_note():
    note = input("Enter your note: ").strip()

    if note:
        notes.append(note)
        print("Note added successfully!")
    else:
        print("Empty notes are not allowed.")