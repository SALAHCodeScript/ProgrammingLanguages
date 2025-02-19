#!python
import tkinter as tk
import salah.gui.tk.tools as tk_tools

app = tk_tools.init(tk, title="Open Folder | SALAH", resolution="600x768")

frame = tk_tools.frame(tk, app)
frame.pack()

label = tk_tools.label(tk, frame, text="Inside a Frame")
label.pack()

app.mainloop()
