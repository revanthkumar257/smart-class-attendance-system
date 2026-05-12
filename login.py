from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from main import FACE_RECOGNITION
import os

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Login")
        self.root.state('zoomed')
        self.root.configure(bg="#F3F4F6")

        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")
        
        # Left side image for design
        try:
            bg_image = Image.open(os.path.join(img_dir, "login.jpg"))
            bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            pass

        # Frame for Login Form
        frame = Frame(self.root, bg="white", highlightbackground="#E5E7EB", highlightthickness=1)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=450, height=520)

        # Top Accent
        accent = Frame(frame, bg="#3B82F6")
        accent.place(x=0, y=0, relwidth=1, height=8)

        title = Label(frame, text="Welcome Back", font=("Helvetica", 28, "bold"), bg="white", fg="#111827")
        title.place(relx=0.5, y=60, anchor=CENTER)
        
        subtitle = Label(frame, text="Sign in to your account", font=("Helvetica", 12), bg="white", fg="#6B7280")
        subtitle.place(relx=0.5, y=100, anchor=CENTER)

        # Username
        Label(frame, text="Username", font=("Helvetica", 12, "bold"), bg="white", fg="#374151").place(x=40, y=150)
        self.username_entry = Entry(frame, font=("Helvetica", 14), bg="#F9FAFB", fg="#111827", bd=1, relief=SOLID)
        self.username_entry.place(x=40, y=180, width=370, height=40)

        # Password
        Label(frame, text="Password", font=("Helvetica", 12, "bold"), bg="white", fg="#374151").place(x=40, y=240)
        self.password_entry = Entry(frame, font=("Helvetica", 14), show='*', bg="#F9FAFB", fg="#111827", bd=1, relief=SOLID)
        self.password_entry.place(x=40, y=270, width=370, height=40)

        # Login Button
        login_btn = Button(frame, text="Sign in", command=self.login, font=("Helvetica", 14, "bold"),
                           bg="#3B82F6", fg="white", activebackground="#2563EB", activeforeground="white", cursor="hand2", bd=0)
        login_btn.place(x=40, y=350, width=370, height=45)

        # Register Button
        register_btn = Button(frame, text="Don't have an account? Register Here", command=self.register_window,
                              font=("Helvetica", 11), bg="white", fg="#3B82F6", activebackground="white", activeforeground="#2563EB", cursor="hand2", bd=0)
        register_btn.place(relx=0.5, y=430, anchor=CENTER)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()

            if result:
                self.open_main_window()
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error: {str(e)}")

    def open_main_window(self):
        self.root.destroy()
        root = Tk()
        app = FACE_RECOGNITION(root)
        root.mainloop()

    def register_window(self):
        self.new_window = Toplevel(self.root)
        Register(self.new_window)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Account")
        self.root.geometry("450x620+500+100")
        self.root.configure(bg="#F3F4F6")

        frame = Frame(self.root, bg="white", highlightbackground="#E5E7EB", highlightthickness=1)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=400, height=580)

        accent = Frame(frame, bg="#10B981")
        accent.place(x=0, y=0, relwidth=1, height=8)

        Label(frame, text="Create Account", font=("Helvetica", 24, "bold"), fg="#111827", bg="white").place(relx=0.5, y=50, anchor=CENTER)
        Label(frame, text="Join the system today", font=("Helvetica", 11), fg="#6B7280", bg="white").place(relx=0.5, y=85, anchor=CENTER)

        y_pos = 130
        Label(frame, text="Username", font=("Helvetica", 11, "bold"), bg="white", fg="#374151").place(x=30, y=y_pos)
        self.username_entry = Entry(frame, font=("Helvetica", 12), bg="#F9FAFB", bd=1, relief=SOLID)
        self.username_entry.place(x=30, y=y_pos+25, width=340, height=35)

        y_pos += 80
        Label(frame, text="Email", font=("Helvetica", 11, "bold"), bg="white", fg="#374151").place(x=30, y=y_pos)
        self.email_entry = Entry(frame, font=("Helvetica", 12), bg="#F9FAFB", bd=1, relief=SOLID)
        self.email_entry.place(x=30, y=y_pos+25, width=340, height=35)

        y_pos += 80
        Label(frame, text="Phone", font=("Helvetica", 11, "bold"), bg="white", fg="#374151").place(x=30, y=y_pos)
        self.phone_entry = Entry(frame, font=("Helvetica", 12), bg="#F9FAFB", bd=1, relief=SOLID)
        self.phone_entry.place(x=30, y=y_pos+25, width=340, height=35)

        y_pos += 80
        Label(frame, text="Password", font=("Helvetica", 11, "bold"), bg="white", fg="#374151").place(x=30, y=y_pos)
        self.password_entry = Entry(frame, font=("Helvetica", 12), show='*', bg="#F9FAFB", bd=1, relief=SOLID)
        self.password_entry.place(x=30, y=y_pos+25, width=340, height=35)

        y_pos += 90
        register_btn = Button(frame, text="Register", command=self.register_user, font=("Helvetica", 14, "bold"),
                              bg="#10B981", fg="white", activebackground="#059669", activeforeground="white", cursor="hand2", bd=0)
        register_btn.place(x=30, y=y_pos, width=340, height=45)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email    = self.email_entry.get()
        phone    = self.phone_entry.get()

        if username == "" or password == "" or email == "" or phone == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email, phone) VALUES (%s, %s, %s, %s)",
                           (username, password, email, phone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
