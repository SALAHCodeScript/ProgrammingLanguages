import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk  # Requires `pip install pillow`

root = tk.Tk()
root.geometry("1360x768")

# Load images
frames = [ImageTk.PhotoImage(Image.open(f"Images\\Walk ({i}).png")) for i in range(1, 10)]
frame_cycle = cycle(frames)  # Loop through frames

label = tk.Label(root)
label.pack()

def animate():
    label.config(image=next(frame_cycle))
    root.after(100, animate)

animate()
root.mainloop()
