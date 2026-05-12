from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Dataset - Smart Class Attendance")
        self.root.configure(bg="#F3F4F6")

        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")

        # Header Frame
        header_frame = Frame(self.root, bg="#1F2937")
        header_frame.place(x=0, y=0, relwidth=1, height=80)

        # Title label
        title_lbl = Label(header_frame, text="TRAIN DATASET", font=("Helvetica", 28, "bold"), bg="#1F2937", fg="white")
        title_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Main Card Frame
        card_frame = Frame(self.root, bg="white", highlightbackground="#D1D5DB", highlightthickness=1)
        card_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=500)
        
        # Add a top border color accent to the card
        accent = Frame(card_frame, bg="#8B5CF6") # Purple accent
        accent.place(x=0, y=0, relwidth=1, height=8)

        # Display images nicely inside the card or just use one main graphic
        try:
            # Load a graphic for the training
            img = Image.open(os.path.join(img_dir, "8.jpeg")) # The graphic from face recognition works here too or main2.jpg
            img = img.resize((300, 200), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            
            img_lbl = Label(card_frame, image=self.photoimg, bg="white", bd=0)
            img_lbl.place(relx=0.5, y=140, anchor=CENTER)
        except:
            pass

        # Text explanation
        desc_title = Label(card_frame, text="Machine Learning Model", font=("Helvetica", 24, "bold"), fg="#111827", bg="white")
        desc_title.place(relx=0.5, y=280, anchor=CENTER)

        desc = "Train the face recognition model with the collected student datasets.\nThis process might take a few minutes depending on the data size."
        desc_lbl = Label(card_frame, text=desc, font=("Helvetica", 12), fg="#4B5563", bg="white", justify=CENTER)
        desc_lbl.place(relx=0.5, y=340, anchor=CENTER)

        # Train Button
        train_btn = Button(card_frame, text="Start Training", command=self.train_classifier, font=("Helvetica", 16, "bold"),
                           bg="#8B5CF6", fg="white", activebackground="#7C3AED", activeforeground="white", cursor="hand2", bd=0)
        train_btn.place(relx=0.5, y=420, anchor=CENTER, width=300, height=50)

    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            return None

    def train_classifier(self):
        data_dir = "data"
        
        # Check if the data directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "No images found in the 'data' folder.")
            return
        
        # Get all images in the data directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]

        faces = []
        ids = []

        # Loop through each image in the directory
        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert image to grayscale
                imageNp = np.array(img, 'uint8')  # Convert image to NumPy array
                
                # Ensure file has a valid naming convention
                filename = os.path.split(image)[1]
                if filename.count('.') < 2:
                    continue
                
                id = int(filename.split('.')[1])  # Extract ID from filename

                faces.append(imageNp)
                ids.append(id)

                # Optional: Show the image being trained
                cv2.imshow("Training", imageNp)
                cv2.waitKey(10)

            except Exception as e:
                continue
        
        if len(faces) == 0:
            messagebox.showerror("Error", "No valid images found for training.")
            return

        ids = np.array(ids)

        try:
            # Train the classifier using LBPH
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)

            # Save the trained classifier to a file
            clf.write("classifier.xml")
            cv2.destroyAllWindows()

            # Show a success message
            messagebox.showinfo("Result", "Training completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error during training: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
