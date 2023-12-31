import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog

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

def choose_filext():
    global file_extension
    global file_extension_dict
    file_extension = None
    file_type = file_type_var.get()

    file_extension_dict = {
        "JPG": ".jpg",
        "JPEG": ".jpeg",
        "MP4": ".mp4",
        "MP3": ".mp3",
        "PNG": ".png",
        "Every picture": [".jpeg", ".jpg", ".png"],
    }

    file_extension = file_extension_dict.get(file_type, None)

    if file_type == "Every picture":
        file_extension = file_extension_dict["Every picture"]

    if not file_extension:
        output_text.inster(tk.END, "Invalid file type selection.\n")
        return
    
def count_method(path, extensions):
    count = 0

    for file in os.listdir(path):
        for extension in extensions:
            if(os.path.splitext(file)[-1].lower() == extension):
                count += 1

    return count

def list_files_with_size(directory_path):
    file_list = os.listdir(directory_path)

    files_with_size = []
    for filename in file_list:
        file_path = os.path.join(directory_path, filename)
        file_size = os.path.getsize(file_path)
        files_with_size.append([filename, file_size])

    return files_with_size


def copy_method(file_extension, source_path, destination_path):
    copied_files = 0

    files = list_files_with_size(source_path)
    existing_files = list_files_with_size(destination_path)

    for file, size in files:
        if os.path.splitext(file)[-1].lower() in file_extension:
            if [file, size] not in existing_files:
                shutil.copy2(os.path.join(source_path, file), destination_path)
                output_text.insert(tk.END, f"Copied {file} to {destination_path} from {source_path}\n")
                copied_files += 1

    return copied_files

def convert_to_list(element):
    if not isinstance(element, list):
        element = [element]

    return element

def copy_files():
    global file_extension, source_path, destination_path

    choose_filext()

    file_extension = convert_to_list(file_extension) # todo refactor

    all_files = count_method(source_path, file_extension)

    output_text.delete(1.0, tk.END)

    copied_files = copy_method(file_extension, source_path, destination_path)

    status_text.config(text = f"Copied {copied_files} files of {all_files}!")

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
file_type_var = tk.StringVar()
file_type_var.set("Select file type")
file_type_dropdown = ttk.Combobox(root, textvariable=file_type_var, values=["Select file type","Every picture", "JPG", "JPEG", "MP4","MP3", "PNG"])
file_type_dropdown.pack()

output_text = tk.Text(root, height=10, width=80)
output_text.pack()

status_text = tk.Label(root, text = "Start moving files...", font = ("Arial", 12)) 
status_text.pack()

root.mainloop()