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
destination_path = None
source_path = None

copy_button = None
swap_button = None

def choose_source_folder():
    global source_path
    source_path = filedialog.askdirectory()
    source_path_label.config(text = "Source folder: " + source_path)

    enable_copy_button()
    enable_swap_button()

def choose_destination_folder():
    global destination_path
    destination_path = filedialog.askdirectory()
    destination_path_label.config(text = "Destination folder: " + destination_path)

    enable_copy_button()
    enable_swap_button()

def enable_swap_button():
    global swap_button
    if destination_path and source_path and swap_button is None:
        swap_button = ttk.Button(root, text = "Swap routes", command = swap_routes)
        swap_button.pack()

def enable_copy_button():
    global copy_button
    if destination_path and source_path and copy_button is None:
        copy_button = ttk.Button(root, text = "Copy files from source to destination", command = copy_files)
        copy_button.pack()

def copy_files():
    output_text.delete(1.0, tk.END)

    for file in os.listdir(source_path):
        shutil.copy2(os.path.join(source_path, file), destination_path)
        output_text.insert(tk.END, f"copied {file} to {destination_path} from {source_path}\n")

    title_label.config(text = "Copy successful!")

def swap_routes():
    global source_path, destination_path
    source_path, destination_path = destination_path, source_path
    source_path_label.config(text = "Source folder: " + source_path)
    destination_path_label.config(text = "Destination folder: " + destination_path)

root = tk.Tk()
root.geometry("800x600")
root.title("File Mover")

title_label = tk.Label(root, text = "Move your files easily", font = ("Arial", 18))
title_label.pack(padx = 25, pady = 25)
source_button = ttk.Button(root, text = "Select source folder", command = choose_source_folder)
source_button.pack()
source_path_label = tk.Label(root, text = "No source folder selected!", font = ("Arial", 12))
source_path_label.pack()
source_button = ttk.Button(root, text = "Select destination folder", command = choose_destination_folder)
source_button.pack()
destination_path_label = tk.Label(root, text = "No destination folder selected!", font = ("Arial", 12))
destination_path_label.pack()

output_text = tk.Text(root, height=10, width=80)
output_text.pack()

root.mainloop()