from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from typing import List

class Application:
    def __init__(self, root: Tk, fields: List[str], buttons: Button, table: List[str]):
        self.conn = sqlite3.connect('data/database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS customer(name, email)")
    
        self.root = root
        self.root.geometry('400x200')
        self.root.title('Customer Register')
        self.root.resizable(False, False)
        self.fields = fields
        self.table = table
        self.buttons = buttons

        # call functions
        self.table_data_view()
        self.buttons_config()
        

    def buttons_config(self) -> None:
        self.buttons[0]['command'] = self.create_db
        self.buttons[1]['command'] = self.delete_db

        # BUTTON TEST
        self.buttons[2]['command'] = self.update_db
    
    def table_select_item(self) -> None:
        _selected_item = self.table.selection()

        if not _selected_item:
            self.table.selection_set(self.table.get_children()[0])
        else:
            next_item = self.table.next(_selected_item[0])
            self.table.selection_set(self.table.next(_selected_item[0]))
            # Se não verificar se há um próximo item a seleção voltará para o início da lista
            if next_item:
                self.table.selection_set(next_item)

    def table_data_view(self) -> None:
        self.table.delete(*self.table.get_children())
        for item in self.read_db():
            self.table.insert("", END, values=item)

    #CRUD FOR DATABE
    def create_db(self) -> None:
        data = []
        for item in self.fields:
            data.append(item.get())
            item.delete(0, END)
            
        if any(element == '' for element in data):
            messagebox.showwarning(title="Empty Fields", message="You need to fill the fields")
        else:
            self.cur.execute("INSERT INTO customer(name, email) VALUES(?, ?)", data)
            self.conn.commit()
            self.table_data_view()
            self.fields[0].focus_set()

    def read_db(self) -> List[str]:
        return self.cur.execute("SELECT * FROM customer").fetchall()
    
    def update_db(self) -> None:
        _selected_item = self.table.selection()
        _entries = []

        if not _selected_item:
            messagebox.showwarning(title="Empty Fields", message="You need to fill the fields")
        else:    
            _edit_window = Toplevel(self.root)
            _edit_window.title('Edit Records')

            for n, item in enumerate(['Name', 'Email']):
                _label = Label(_edit_window, text=item, font='Verdana 10 bold')
                _label.grid(column=n, row=0, sticky=W, padx=2)
                _entry = Entry(_edit_window)
                _entry.grid(column=n, row=1)
                _entry.insert(0, self.table.item(_selected_item)['values'][n])
                _entries.append(_entry)

            def update_data():
                x = []
                y = self.table.item(self.table.selection())['values'][0]
                for item in _entries:
                    x.append(item.get())
                    item.delete(0, END)
                self.cur.execute("UPDATE customer SET name=?, email=? WHERE name=?", (x[0], x[1], y,))
                self.conn.commit()
                self.table_data_view()
                messagebox.showinfo(title='Data Updated', message='Your record has been updated!')
                _edit_window.destroy()

            _button_submit = Button(_edit_window, text='Submit', command=update_data)
            _button_submit.grid(column=0, columnspan=2, row=2, pady=2, sticky=NSEW)

    def delete_db(self) -> None:
        _message_str = "You are about to permanently delete a record from the database"
    
        _selected_item = self.table.selection()
        if not _selected_item:
            messagebox.showwarning(title='No data selected', message='Any data Selected')
        else:
            _message_confirm = messagebox.askquestion(title='Are you sure?', message=_message_str)
            if _message_confirm == 'yes':
                data = self.table.item(_selected_item)['values'][0]
                self.cur.execute("DELETE FROM customer WHERE name=?", (data,))
                self.conn.commit()
                self.table_data_view()
                messagebox.showinfo(title='Data Deleted', message='Your record has been deleted!')
    #END CRUD FOR DATABASE

    def start_app(self) -> None:
        self.root.mainloop()