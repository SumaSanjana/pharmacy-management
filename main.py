import tkinter as tk
from tkinter import ttk

def open_main_app():
    main_app_window = tk.Toplevel(root)
    main_app_window.title("Cure&Care Main Application")
    main_app_label = ttk.Label(main_app_window, text="Welcome to Cure&Care!")
    main_app_label.pack()

def animate_caption():
    def change_color():
        new_color = "blue" if current_color == "black" else "black"
        welcome_label.config(foreground=new_color)
        root.after(1000, change_color)

    change_color()

root = tk.Tk()
root.title("Cure&Care Welcome Page")

width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

get_started_button = ttk.Button(root, text="Get Started", command=open_main_app)
get_started_button.pack(pady=30)

animate_caption()

root.mainloop()
