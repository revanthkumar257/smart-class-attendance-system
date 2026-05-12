from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from time import strftime
from datetime import datetime
import mysql.connector
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#F3F4F6")
        
        # Header Label
        header_frame = Frame(self.root, bg="#1F2937")
        header_frame.place(x=0, y=0, relwidth=1, height=80)
        
        title_lbl = Label(header_frame, text="FACE RECOGNITION", font=("Helvetica", 28, "bold"), bg="#1F2937", fg="white")
        title_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images", "images")

        # Container placed a bit higher, fixed height to fit smaller screens
        container = Frame(self.root, bg="#F3F4F6")
        container.place(relx=0.5, y=90, anchor=N, width=1100, height=580)

        # Left Image
        try:
            img_left = Image.open(os.path.join(img_dir, "face1.jpeg"))  
            img_left = img_left.resize((500, 420), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            left_lbl = Label(container, image=self.photoimg_left, bd=2, relief=SOLID)
            left_lbl.place(x=20, y=10)
        except:
            pass

        # Right Image
        try:
            img_right = Image.open(os.path.join(img_dir, "8.jpeg")) 
            img_right = img_right.resize((500, 420), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
            right_lbl = Label(container, image=self.photoimg_right, bd=2, relief=SOLID)
            right_lbl.place(x=580, y=10)
        except:
            pass
        
        # Bottom text / card
        action_card = Frame(container, bg="white", highlightbackground="#D1D5DB", highlightthickness=1)
        action_card.place(relx=0.5, y=450, anchor=N, width=800, height=100)

        Label(action_card, text="Ready to start recognition?", font=("Helvetica", 16, "bold"), bg="white", fg="#111827").place(x=50, rely=0.5, anchor=W)
        
        # Button
        btn = Button(action_card, text="Face Recognition", command=self.recognize_face, font=("Helvetica", 16, "bold"), bg="#EF4444", fg="white", activebackground="#DC2626", activeforeground="white", cursor="hand2", bd=0)
        btn.place(x=550, rely=0.5, anchor=W, width=200, height=50)
    
    def mark_attendence(self, name, roll, dep):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [entry.split(",")[0] for entry in myDataList]

            if name not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                # format: name, roll, dept, time, date, status
                f.writelines(f"\n{name},{roll},{dep},{dtString},{d1},present")
    
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray[y:y + h, x:x + w])
            confidence = int((100) * (1 - (predict / 300)))

            try:
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="1234", 
                    database="face_recognition"
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student_Name FROM student WHERE Student_id = %s", (id,))
                i = my_cursor.fetchone()
                name = "+".join(i) if i else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (id,))
                r = my_cursor.fetchone()
                roll = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (id,))
                d = my_cursor.fetchone()
                dep = "+".join(d) if d else "Unknown"
                
                conn.close()
            except Exception as e:
                name = "Unknown"
                roll = "Unknown"
                dep = "Unknown"

            if confidence > 77:
                cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Dep: {dep}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll: {roll}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendence(name, roll, dep)
            else:
                cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)

            coord = [x, y, w, h]

        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
        return img

    def recognize_face(self):
        faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # Start the webcam
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        retries = 0
        import time

        while True:
            ret, img = cap.read()
            if not ret:
                retries += 1
                if retries > 50:
                    break
                time.sleep(0.1)
                continue
            
            retries = 0

            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Face Scanner", img)

            # Keep Tkinter responsive
            self.root.update()

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break
                
            try:
                if cv2.getWindowProperty("Face Scanner", cv2.WND_PROP_VISIBLE) < 1:
                    break
            except cv2.error:
                pass

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()