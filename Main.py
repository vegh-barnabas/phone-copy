import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog

# OS
# src = r"D:\moving"
# dst = r"D:\movehere"

# extjpg = ".jpg"
# extpng = ".png"

# for file in os.listdir(src):
#     if os.path.splitext(file) [-1] == extjpg or extpng:
#         shutil.move(os.path.join(src, file), dst)

# TKinter
def choose_folder():
    source_path = filedialog.askdirectory()
    print(source_path)

    source_path_label = tk.Label(root, text = "Source folder: " + source_path, font = ("Arial", 12))
    source_path_label.pack()

root = tk.Tk()
root.geometry("800x600")
root.title("File Mover")

title_label = tk.Label(root, text = "Move your files easily", font = ("Arial", 18))
title_label.pack(padx = 25, pady = 25)
source_button = ttk.Button(root, text = "Select source folder", command = choose_folder)
source_button.pack()

root.mainloop()