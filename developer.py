from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#F3F4F6")
        
        # Header Label
        title_lbl = Label(self.root, text="MEET THE DEVELOPER", font=("Helvetica", 26, "bold"), bg="#1F2937", fg="white", pady=10)
        title_lbl.place(x=0, y=0, relwidth=1, height=70)
        
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")
        
        # Load Background Image
        try:
            img_top = Image.open(os.path.join(img_dir, "dev.png"))
            img_top = img_top.resize((1530, 720), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            
            f_lbl = Label(self.root, image=self.photoimg_top)
            f_lbl.place(x=0, y=70, relwidth=1, height=720)
        except:
            f_lbl = Frame(self.root, bg="#F3F4F6")
            f_lbl.place(x=0, y=70, relwidth=1, height=720)
            
        # Semi-transparent overlay or solid card for developer info
        card_frame = Frame(f_lbl, bg="white", highlightbackground="#D1D5DB", highlightthickness=1)
        card_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=650, height=480)
        
        # Add a top border color accent to the card
        accent = Frame(card_frame, bg="#3B82F6")
        accent.place(x=0, y=0, relwidth=1, height=8)

        # Developer Image
        try:
            # You can change 'dev.png' to an actual profile picture file if available
            img_dev = Image.open(os.path.join(img_dir, "dev.png")) 
            img_dev = img_dev.resize((160, 160), Image.LANCZOS)
            self.photoimg_dev = ImageTk.PhotoImage(img_dev)
            
            # Using a solid border around the image to make it stand out
            img_lbl = Label(card_frame, image=self.photoimg_dev, bg="white", bd=3, relief=SOLID)
            img_lbl.place(relx=0.5, y=130, anchor=CENTER)
        except Exception as e:
            print(f"Image not found: {e}")

        # Developer Details
        name_lbl = Label(card_frame, text="Revanth Kumar", font=("Helvetica", 32, "bold"), fg="#111827", bg="white")
        name_lbl.place(relx=0.5, y=260, anchor=CENTER)
        
        # Professional tag or short bio
        bio_lbl = Label(card_frame, text="Creator & Lead Developer", font=("Helvetica", 14, "italic"), fg="#3B82F6", bg="white")
        bio_lbl.place(relx=0.5, y=310, anchor=CENTER)
        
        # Description
        desc = "Driving the Smart Class Attendance System project.\nPassionate about building scalable and impactful software solutions."
        desc_lbl = Label(card_frame, text=desc, font=("Helvetica", 12), fg="#4B5563", bg="white", justify=CENTER)
        desc_lbl.place(relx=0.5, y=370, anchor=CENTER)
        
        # Optional contact / link info
        contact_lbl = Label(card_frame, text="revanthyadavg05@gmail.com", font=("Helvetica", 12, "bold"), fg="#6B7280", bg="white")
        contact_lbl.place(relx=0.5, y=430, anchor=CENTER)

if __name__ == "__main__":
    root = Tk()
    root.update_idletasks()
    obj = Developer(root)
    root.mainloop()
