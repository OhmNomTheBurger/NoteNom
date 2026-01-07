import os
import sys
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox

# Set appearance mode and color theme
background_main_color = "#282828"
entry_color = "#353535"
middle_color = "#3A3A3A"
button_color = "#353535"
button_hover_color = "#353535"

# Create Tkinter window
root = ctk.CTk(fg_color=background_main_color)
root.title("NoteNom")
root.geometry("600x300")

# track current open file (None = unsaved / new)
current_file = None

#resource path function
def resource_path(relative_path: str) -> str:
    """Return an absolute path to a resource, works for dev and PyInstaller bundle."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Set window icon
root.iconbitmap(resource_path("notes.ico"))

#black and light mode toggle function
def totgle_mode(parent):
    combobox = ctk.CTkComboBox(
        parent,
        values=["Dark Mode", "Light Mode"],
        width=200,
        height=30,
        fg_color=middle_color,
        font=("Geneva", 14),
        border_width=0,
        corner_radius=10,
        text_color="white",
        command=lambda choice: ctk.set_appearance_mode(choice.split()[0]),
    )
    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("Light")
        combobox.set("Light Mode")
    else:
        ctk.set_appearance_mode("Dark")
        combobox.set("Dark Mode")
    return combobox


# --- File controls: open / save ---
def save_file():
    global current_file
    try:
        content = widget_text.get("1.0", "end-1c")
        if not current_file:
            return save_file_as()
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(content)
        root.title(f"NoteNom - {os.path.basename(current_file)}")
        return True
    except Exception as e:
        messagebox.showerror("Save Error", str(e))
        return False


def save_file_as():
    global current_file
    try:
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not path:
            return False
        current_file = path
        return save_file()
    except Exception as e:
        messagebox.showerror("Save As Error", str(e))
        return False


def open_file():
    global current_file
    try:
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not path:
            return False
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        widget_text.delete("1.0", "end")
        widget_text.insert("1.0", data)
        current_file = path
        root.title(f"NoteNom - {os.path.basename(current_file)}")
        return True
    except Exception as e:
        messagebox.showerror("Open Error", str(e))
        return False


# Create a top frame for controls (combobox + buttons)
top_frame = ctk.CTkFrame(root, fg_color=background_main_color, border_width=0)
top_frame.pack(fill=ctk.X)

# add combobox into top_frame
top_combobox = totgle_mode(top_frame)
top_combobox.pack(side=ctk.LEFT, padx=10, pady=(10, 6))

# add Open and Save buttons on the right
open_btn = ctk.CTkButton(top_frame, text="Open", width=80, command=open_file, fg_color=button_color, hover_color=button_hover_color, text_color="white")
open_btn.pack(side=ctk.RIGHT, padx=10, pady=8)
save_btn = ctk.CTkButton(top_frame, text="Save", width=80, command=save_file, fg_color=button_color, hover_color=button_hover_color, text_color="white")
save_btn.pack(side=ctk.RIGHT, padx=10, pady=8)

# Text widget (placed below the top frame so both resize naturally)
widget_text = ctk.CTkTextbox(root, width=580, height=240, fg_color=entry_color, wrap="word", font=("Geneva", 20), border_width=0, corner_radius=20)
widget_text.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Bind Ctrl+S to save
root.bind("<Control-s>", lambda e: save_file())

# Run the application
root.mainloop() 