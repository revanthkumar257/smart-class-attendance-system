from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Help Desk")
        self.root.configure(bg="#F3F4F6")
        
        # Header Label
        title_lbl = Label(self.root, text="HELP DESK & SUPPORT", font=("Helvetica", 26, "bold"), bg="#1F2937", fg="white", pady=10)
        title_lbl.place(x=0, y=0, relwidth=1, height=70)
        
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")
        
        # Semi-transparent overlay or solid card for help info
        card_frame = Frame(self.root, bg="white", highlightbackground="#D1D5DB", highlightthickness=1)
        card_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=650, height=480)
        
        # Add a top border color accent to the card
        accent = Frame(card_frame, bg="#10B981") # Green accent for support
        accent.place(x=0, y=0, relwidth=1, height=8)

        # Help Icon / Image
        try:
            img_help = Image.open(os.path.join(img_dir, "7.png")) # Using the help desk icon from main.py
            img_help = img_help.resize((160, 160), Image.LANCZOS)
            self.photoimg_help = ImageTk.PhotoImage(img_help)
            
            img_lbl = Label(card_frame, image=self.photoimg_help, bg="white", bd=0)
            img_lbl.place(relx=0.5, y=140, anchor=CENTER)
        except:
            pass

        # Title Text
        help_title = Label(card_frame, text="How can we help you?", font=("Helvetica", 28, "bold"), fg="#111827", bg="white")
        help_title.place(relx=0.5, y=260, anchor=CENTER)
        
        # Description
        desc = "If you are facing any issues with the Smart Class Attendance System,\nplease reach out to our dedicated support team."
        desc_lbl = Label(card_frame, text=desc, font=("Helvetica", 12), fg="#4B5563", bg="white", justify=CENTER)
        desc_lbl.place(relx=0.5, y=320, anchor=CENTER)
        
        # Contact info
        contact_lbl = Label(card_frame, text="Email Support:", font=("Helvetica", 14), fg="#6B7280", bg="white")
        contact_lbl.place(relx=0.5, y=380, anchor=CENTER)

        email_lbl = Label(card_frame, text="revanthyadavg05@gmail.com", font=("Helvetica", 16, "bold"), fg="#3B82F6", bg="white")
        email_lbl.place(relx=0.5, y=415, anchor=CENTER)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
