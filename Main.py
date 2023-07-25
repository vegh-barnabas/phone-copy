import os
import shutil
import tkinter as tk
from tkinter import ttk

src = r"H:\moving"
dst = r"F:\movehere"

extjpg = ".jpg"
extpng = ".png"

for file in os.listdir(src):
    if os.path.splitext(file) [-1] == extjpg or extpng:
        shutil.move(os.path.join(src, file), dst)

root = tk.Tk()
root.geometry("800x600")
root.title("File Mover")

label = tk.Label(root, text ="Move your files easily", font=("Arial", 18))
label.pack(padx=25, pady=25)

def on_dropdown_selected(event):
    selected_item = dropdown_var.get()
    print(f"Selected item: {selected_item}")

dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=["Option 1", "Option 2", "Option 3"])
dropdown.set("Select an option")

dropdown.bind("<<ComboboxSelected>>", on_dropdown_selected)
dropdown.pack()

root.mainloop()