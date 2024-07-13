import tkinter as tk
from tools.getPath import get_resource_path
from tools.readText import read_text


def trigger_read_text():
    if minimize_while_reading.get() == 1:
        root.iconify()
    root.update()
    text_val = read_text()
    if not text_val:
        text_val = "No Text detected"
        text_field.configure(fg="red")
    else:
        text_field.configure(fg="black")
    text_field.configure(state="normal")
    text_field.delete("1.0", "end")
    text_field.insert("1.0", text_val)
    if auto_copy.get() == 1:
        copy_text()
    text_field.configure(state="disabled")
    if minimize_while_reading.get() == 1:
        root.deiconify()  # Restores the window from taskbar


def copy_text():
    root.clipboard_clear()
    text = text_field.get("1.0", 'end-1c')
    root.clipboard_append(text)


def always_on_top():
    root.attributes('-topmost', always_on_top_option.get())


root = tk.Tk()
root.title("Scrext")
icon_path = get_resource_path('images/kitty.ico')
root.iconbitmap(icon_path)
root.geometry('300x200')
# Settings--------------------------------------------------------------------------------------------------------------
menubar = tk.Menu(root)
root.config(menu=menubar)

settings = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Settings', menu=settings)

auto_copy = tk.IntVar(value=1)
settings.add_checkbutton(label='Auto Copy', variable=auto_copy)

always_on_top_option = tk.IntVar(value=1)
settings.add_checkbutton(label='Always on Top', variable=always_on_top_option, command=always_on_top)

minimize_while_reading = tk.IntVar(value=1)
settings.add_checkbutton(label='Minimize while Reading', variable=minimize_while_reading)
# ----------------------------------------------------------------------------------------------------------------------

text_field = tk.Text(root, bg="#faf4de", state="disabled")
text_field.grid(row=0, column=0, sticky='nsew')

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky='ns')

text_field.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_field.yview)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

button = tk.Button(root, text="Start selecting your Area", command=trigger_read_text)
button.grid(row=1, column=0, columnspan=2, sticky='ew')

if __name__ == "__main__":
    root.mainloop()
