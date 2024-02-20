import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory


def select_file_dialog(entry):
    def f():
        d = askdirectory()
        entry.delete(0, tk.END)
        entry.insert(0, d)
    return f


def make_file_entry(name):
    frame = ttk.LabelFrame(text=name)
    ent = ttk.Entry(frame)
    btn = ttk.Button(frame, text='...', command=select_file_dialog(ent))
    ent.grid(row=0, column=0, columnspan=4)
    btn.grid(row=0, column=8)
    frame.pack()
    return frame


def make_entry(name, entry_type, default_val):
    f = ttk.LabelFrame(text=name)
    match entry_type:
        case 'bool':
            ent = ttk.Checkbutton(f)
        case other:
            ent = ttk.Entry(f)
            ent.insert(0, str(default_val))
            
    f.pack(pady=10)
    ent.pack()
    return ent


def make_window():
    # Entry info
    entry_args = [
        ('Start Section', 'int', ''),
        ('End Section', 'int', ''),
        ('X-Overlap', 'float', 7.2),
        ('Y-Overlap', 'float', 7.2),
        ('Channel', 'int', 0),
        ('Average Correction?', 'bool', ''),
        ('Downsize Amount', 'int', '')
    ]

    # Initialise window
    window = tk.Tk(screenName='DeepCATs Stitching', baseName="deepcats", className='deepcats')
    window.minsize(800, 200)
    
    # Entries
    file_ents = make_file_entry('TC Path')
    fields = [ make_entry(*args) for args in entry_args ]
 
    # Button
    submit = ttk.Button(text='Stitch')
    submit.pack(pady=20)

    # Start Loop
    window.mainloop()


make_window()