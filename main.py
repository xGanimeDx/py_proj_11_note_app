import json
import uuid
from datetime import date
from tkinter import *

def save_to_json(message):
    data = {'id': str(uuid.uuid4()), 'message': message, 'time': date.today()}
    with open('notes.json', 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data['notes'].append(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def add_note(text):
    message = text.get('1.0', 'end-1c')
    save_to_json(message)
    text.delete('1.0', END)

def open_add_note_window():
    add_note_window = Toplevel()
    add_note_window.geometry('267x165+950+300')
    add_note_window.title('Add Note')

    # widgets
    note_message_frame = LabelFrame(add_note_window, text='Enter note message:')
    note_message_input = Text(note_message_frame, height=3, width=35)
    add_button = Button(add_note_window, text='Add', command=lambda: add_note(note_message_input))
    close_button = Button(add_note_window, text='Close', command=add_note_window.destroy)

    # place widgets
    note_message_frame.place(x=5, y=5)
    note_message_input.pack()
    add_button.place(x=5, y=75)
    close_button.place(x=65, y=75)

# root widget
root = Tk()
root.geometry('600x300+300+300')
root.title('note App')

# widgets
add_note_button = Button(root, text='Add note', command=open_add_note_window)
quit_button = Button(root, text='Quit', command=root.quit)


# place widgets
add_note_button.place(x=5, y=5)
quit_button.place(x=100, y=5)

root.mainloop()
