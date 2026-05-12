from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from time import strftime
from datetime import datetime

from developer import Developer
from help import Help
from train import  Train
from attendance import Attendance
from face_recognition import Face_Recognition
from student import Student
import os

class FACE_RECOGNITION:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Class Attendance System")
        self.root.configure(bg="#F3F4F6")

        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")

        # Header Frame
        header_frame = Frame(self.root, bg="#1F2937")
        header_frame.place(x=0, y=0, relwidth=1, height=80)

        # Title label
        title_lbl = Label(header_frame, text="SMART CLASS ATTENDANCE SYSTEM", font=("Helvetica", 28, "bold"), bg="#1F2937", fg="white")
        title_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Time Label
        self.lbl_time = Label(header_frame, font=('Helvetica', 16, 'bold'), bg='#1F2937', fg='#9CA3AF')
        self.lbl_time.place(x=20, rely=0.5, anchor=W)
        self.time()

        # Try to load a nice background, otherwise keep it flat
        try:
            bg_image = Image.open(os.path.join(img_dir, "4.jpg"))
            # Make it slightly opaque or darker to make buttons pop
            bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()-80), Image.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(bg_image)
            bg_lbl = Label(self.root, image=self.photoimg_bg)
            bg_lbl.place(x=0, y=80, relwidth=1, relheight=1)
        except:
            bg_lbl = Frame(self.root, bg="#F3F4F6")
            bg_lbl.place(x=0, y=80, relwidth=1, relheight=1)

        # Create centered grid for buttons
        grid_frame = Frame(bg_lbl, bg="white", highlightbackground="#D1D5DB", highlightthickness=1)
        grid_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=900, height=550)

        # Title inside grid
        Label(grid_frame, text="Dashboard", font=("Helvetica", 24, "bold"), bg="white", fg="#111827").place(relx=0.5, y=40, anchor=CENTER)

        self.create_buttons(grid_frame)

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl_time.config(text=string)
        self.lbl_time.after(1000, self.time)

    def load_image(self, path, size):
        if not os.path.exists(path):
            return None
        img = Image.open(path).resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def create_buttons(self, parent):
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")
        
        button_config = [
            ("Student Details", os.path.join(img_dir, "student.jpg"), self.student_details),
            ("Face Detector", os.path.join(img_dir, "face2.jpeg"), self.face_data),
            ("Attendance", os.path.join(img_dir, "6.jpeg"), self.attendance),
            ("Help Desk", os.path.join(img_dir, "7.png"), self.help),
            ("Train Data", os.path.join(img_dir, "8.jpeg"), self.train_data),
            ("Photos", os.path.join(img_dir, "9.jpeg"), self.open_img),
            ("Developer", os.path.join(img_dir, "10.jpeg"), self.developer),
            ("Exit", os.path.join(img_dir, "11.jpeg"), self.exit_system)
        ]

        # Button layout inside the grid_frame (width 900, height 550)
        start_x = 75
        start_y = 90
        x, y = start_x, start_y
        for i, (text, img_path, command) in enumerate(button_config):
            if i == 4:  # Move to next row
                x, y = start_x, start_y + 220
            self.create_card_button(parent, img_path, text, x, y, command)
            x += 195

    def create_card_button(self, parent, img_path, text, x, y, command):
        """Create a styled button card."""
        card = Frame(parent, bg="#F9FAFB", highlightbackground="#E5E7EB", highlightthickness=1)
        card.place(x=x, y=y, width=160, height=190)
        
        img = self.load_image(img_path, (120, 120))
        if img:
            btn = Button(card, image=img, cursor="hand2", command=command, bd=0, bg="#F9FAFB", activebackground="#F3F4F6")
            btn.image = img
            btn.place(relx=0.5, y=70, anchor=CENTER)
            
        Button(card, text=text, command=command, font=("Helvetica", 11, "bold"), bg="#3B82F6", fg="white", bd=0, cursor="hand2", activebackground="#2563EB", activeforeground="white").place(x=0, y=150, width=160, height=40)

    # Button actions
    def open_img(self):
        os.startfile("data")

    def student_details(self):
        if hasattr(self, 'student_window') and self.student_window.winfo_exists():
            self.student_window.lift()
        else:
            self.student_window = Toplevel(self.root)
            self.app = Student(self.student_window)

    def face_data(self):
        if hasattr(self, 'face_window') and self.face_window.winfo_exists():
            self.face_window.lift()
        else:
            self.face_window = Toplevel(self.root)
            self.app = Face_Recognition(self.face_window)

    def attendance(self):
        if hasattr(self, 'attendance_window') and self.attendance_window.winfo_exists():
            self.attendance_window.lift()
        else:
            self.attendance_window = Toplevel(self.root)
            self.app = Attendance(self.attendance_window)

    def help(self):
        if hasattr(self, 'help_window') and self.help_window.winfo_exists():
            self.help_window.lift()
        else:
            self.help_window = Toplevel(self.root)
            self.app = Help(self.help_window)

    def train_data(self):
        if hasattr(self, 'train_window') and self.train_window.winfo_exists():
            self.train_window.lift()
        else:
            self.train_window = Toplevel(self.root)
            self.app = Train(self.train_window)

    def developer(self):
        if hasattr(self, 'developer_window') and self.developer_window.winfo_exists():
            self.developer_window.lift()
        else:
            self.developer_window = Toplevel(self.root)
            self.app = Developer(self.developer_window)

    def exit_system(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = FACE_RECOGNITION(root)
    root.mainloop()
