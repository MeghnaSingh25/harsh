import tkinter as tk
from tkinter import filedialog, messagebox

# ---------- functions ----------

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file = filedialog.askopenfile(filetypes=[("Text Files", "*.txt")])
    if file:
        text.delete("1.0", tk.END)
        text.insert(tk.END, file.read())

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text Files", "*.txt")])
    if file:
        file.write(text.get("1.0", tk.END))
        messagebox.showinfo("Saved", "File saved successfully!")

# ---------- UI ----------

root = tk.Tk()
root.title("Notes 📝")
root.geometry("600x500")

# menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# text area
text = tk.Text(root, font=("Arial", 14), wrap="word")
text.pack(expand=True, fill="both")

root.mainloop()
