import os
import sys
import tkinter as tk
from tkinter import ttk

# Create Tkinter window
root = tk.Tk()
root.title("NoteNom")
root.configure(bg="#2C2B2B")
root.geometry("600x300")

def resource_path(relative_path: str) -> str:
    """Return an absolute path to a resource, works for dev and PyInstaller bundle."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

root.iconbitmap(resource_path("notes.ico"))

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Vertical.TScrollbar",
    background="grey",        # slider
    troughcolor="#676565",     # track
    bordercolor="black",
    arrowcolor="white",
    lightcolor="black",
    darkcolor="grey"
)

# Text widget
text = tk.Text(root, wrap="word", font=("Arial", 14), bg="#353535", fg="white",insertbackground="white")
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=40)


#scrollbar
scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)

root.mainloop()
