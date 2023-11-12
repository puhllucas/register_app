from tkinter import *
from tkinter import ttk
from typing import List

def create_root() -> Tk:
    root = Tk()
    return root

def create_fields(root) -> List[Entry]:
    _frame = Frame(root)
    _frame.place(relx=0, rely=0)
    
    data: List[Entry] = []
    for n, item in enumerate(['Name', 'Email'], start=0):
        _label = Label(_frame, text=item, font='Verdana 10 bold')
        _label.grid(column=n, row=0, sticky=W, padx=2)
        _entry = Entry(_frame, width=23)
        _entry.grid(column=n, row=1, padx=2)
        data.append(_entry)
    return data    

def create_buttons(root) -> List[Button]:
    _frame = Frame(root)
    _frame.place(relx=0, rely=0.228)

    # NEED TO IMPLEMENT LOOP!
    _button_submit = Button(_frame, text='Submit', width=12)
    _button_submit.grid(column=0, row=0, padx=2)

    _button_delete = Button(_frame, text='Delete', width=12)
    _button_delete.grid(column=1, row=0, padx=3)

    #_button_close = Button(_frame, text='Close', width=12)
    #_button_close.grid(column=2, row=0, padx=3)

    _button_test = Button(_frame, text='Edit', width=12)
    _button_test.grid(column=2, row=0, padx=3)

    data: List[Entry] = [_button_submit, _button_delete, _button_test]

    return data

def create_table(root) -> List[str]:
    _frame = Label(root)
    _frame.place(relx=0, rely=0.395, relwidth=0.96, relheight=0.585)

    _table_columns = ['Name', 'Email']  
    _table = ttk.Treeview(_frame, columns=_table_columns, show='headings', height=10)
    _table.grid(column=0, row=0, padx=2)

    _scroll = ttk.Scrollbar(root, orient=VERTICAL, command=_table.yview)
    _scroll.place(relx=0.96, rely=0.4, relheight=0.588)

    _table.configure(yscrollcommand=_scroll.set)

    for item in _table_columns:
        _table.heading(item, text=item)

    return _table