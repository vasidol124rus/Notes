import datetime
import json
import os


class NotesApp:
    def __init__(self):
        self.notes = []

    def create_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = {
            "id": note_id,
            "title": title,
            "body": body,
            "timestamp": timestamp
        }
        self.notes.append(note)
        print("Note created successfully.")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = new_title
                note['body'] = new_body
                note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Note edited successfully.")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                print("Note deleted successfully.")
                return
        print("Note not found.")

    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)
        print("Notes saved successfully.")

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
            print("Notes loaded successfully.")
        else:
            print("No saved notes found.")

app = NotesApp()

while True:
    print("\nOptions:")
    print("1. Create Note")
    print("2. List Notes")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Save Notes")
    print("6. Load Notes")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the title of the note: ")
        body = input("Enter the body of the note: ")
        app.create_note(title, body)
    elif choice == '2':
        app.list_notes()
    elif choice == '3':
        note_id = int(input("Enter the ID of the note to edit: "))
        new_title = input("Enter the new title of the note: ")
        new_body = input("Enter the new body of the note: ")
        app.edit_note(note_id, new_title, new_body)
    elif choice == '4':
        note_id = int(input("Enter the ID of the note to delete: "))
        app.delete_note(note_id)
    elif choice == '5':
        app.save_notes()
    elif choice == '6':
        app.load_notes()
    elif choice == '7':
        print("Thank you for using my program")
        print("Until next time")
        break
    else:
        print("Invalid choice, please try again.")            