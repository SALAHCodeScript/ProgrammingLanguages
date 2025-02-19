def init(tk, title="Initialization | SALAH", background="#050508", resolution="1360x768"):
    app = tk.Tk()
    app.title(title)
    app.config(background=background)
    app.geometry(resolution)
    return app

def label(tk, app, text="Label", fg="#050508", bg="#969696", font=("0xProto Nerd Font Mono", 20, "normal"), **args):
    return tk.Label(app, text=text, fg=fg, bg=bg, font=font, relief="solid", bd=0, padx=0, pady=0, **args)

def entry(tk, app, text="Label", fg="#050508", bg="#969696", font=("0xProto Nerd Font Mono", 20, "normal"), **args):
    return tk.Entry(app, font=font, relief="solid", bd=0, **args)

def button(tk, app, text="Button", fg="#050508", bg="#969696", activefg="#969696", activebg="#050508", font=("0xProto Nerd Font Mono", 20, "normal"), **args):
    return tk.Button(app, text=text, fg=fg, bg=bg, activeforeground=activefg, activebackground=activebg, font=font, bd=0, padx=0, pady=0, **args)

def frame(tk, app, bg="#969696", **args):
    return tk.Frame(app, bg=bg, relief="solid", bd=0, padx=0, pady=0, **args)
