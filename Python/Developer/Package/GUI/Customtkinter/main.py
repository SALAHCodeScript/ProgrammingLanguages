import customtkinter as ctk

# Initialize the app
ctk.set_appearance_mode("dark")  # "light", "dark", or "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app = ctk.CTk()
app.geometry("400x350")
app.title("Login Form")

# Frame for login form
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

# Title Label
label = ctk.CTkLabel(master=frame, text="Login", font=("Arial", 24, "bold"))
label.pack(pady=20)

# Username Entry
username_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
username_entry.pack(pady=10, padx=20, fill="x")

# Password Entry
password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_entry.pack(pady=10, padx=20, fill="x")

# Remember Me Checkbox
remember_me = ctk.CTkCheckBox(master=frame, text="Remember Me")
remember_me.pack(pady=5)

# Login Button
def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")  # For demonstration
    label.configure(text="Login Successful!" if username == "salah" and password == "sal" else "Invalid Login")

login_button = ctk.CTkButton(master=frame, text="Login", command=login)
login_button.pack(pady=20)

# Run the app
app.mainloop()
