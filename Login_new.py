import customtkinter as ctk
from tkinter import messagebox
import sqlite3

# Initialize the main window
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
root.title("Login Form")
root.geometry("500x600")
root.resizable(True, True)

# Variables
username = ctk.StringVar()
password = ctk.StringVar()

# Background Frame
frame = ctk.CTkFrame(root, width=500, height=600, fg_color=("#ffffff", "#e3f2fd"))
frame.pack(fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(frame, text="Welcome!", font=("Arial", 28, "bold"), text_color="#0078D7")
title_label.place(x=120, y=50)

# Username Entry
username_entry = ctk.CTkEntry(frame, placeholder_text="Username", textvariable=username, width=300, height=40, corner_radius=10)
username_entry.place(x=100, y=150)

# Password Entry
password_entry = ctk.CTkEntry(frame, placeholder_text="Password", textvariable=password, show="*", width=300, height=40, corner_radius=10)
password_entry.place(x=100, y=220)

# Login Function
def login():
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        c.execute("SELECT * FROM admin_registration WHERE username = ? AND password = ?", (username.get(), password.get()))
        result = c.fetchone()
        
        if result:
            messagebox.showinfo("Success", "Login Successful!")
            root.destroy()
            from subprocess import call
            call(["python","GUI_Master_old.py"])

        else:
            messagebox.showerror("Error", "Invalid Username or Password")

# Login Button
login_button = ctk.CTkButton(frame, text="Login", command=login, width=300, height=40, fg_color="#0078D7", hover_color="#005BB5", corner_radius=10)
login_button.place(x=100, y=300)

# Register Function
def registration():
    from subprocess import call
    call(["python", "registration.py"])
    root.destroy()

# Signup Button
signup_button = ctk.CTkButton(frame, text="Sign Up", command=registration, width=300, height=40, fg_color="#E53935", hover_color="#C62828", corner_radius=10)
signup_button.place(x=100, y=360)

# Forgot Password Function
def forgot_password():
    forgot_window = ctk.CTkToplevel(root)
    forgot_window.title("Forgot Password")
    forgot_window.geometry("400x300")

    ctk.CTkLabel(forgot_window, text="Forgot Password", font=("Arial", 20, "bold")).pack(pady=20)

    email_var = ctk.StringVar()
    email_entry = ctk.CTkEntry(forgot_window, placeholder_text="jangidprerana790@gmail.com", textvariable=email_var, width=300)
    email_entry.pack(pady=10)

    def reset_password():
        email = email_var.get()
        if not email:
            messagebox.showwarning("Input Error", "Please enter your email.")
            return
        # Placeholder logic for demonstration
        messagebox.showinfo("Reset Link Sent", f"A password reset link has been sent to {email}.")
        forgot_window.destroy()

    reset_btn = ctk.CTkButton(forgot_window, text="Reset Password", command=reset_password, width=200)
    reset_btn.pack(pady=20)

# Forgot Password Label as Button
forgot_label = ctk.CTkButton(frame, text="Forgot Password?", command=forgot_password, fg_color="transparent", hover_color="#E3F2FD", text_color="#0078D7", width=300, height=30)
forgot_label.place(x=100, y=420)

root.mainloop()
