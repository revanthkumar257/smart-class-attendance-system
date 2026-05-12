# Smart Class Attendance System

A modern, desktop-based Smart Class Attendance System built using Python, Tkinter, and OpenCV. This application uses facial recognition to automate student attendance tracking and provides a comprehensive management interface with a sleek, SaaS-style UI.

## Features

- **Facial Recognition Attendance**: Automatically recognize students using their webcam and mark their attendance.
- **Student Management**: Full CRUD (Create, Read, Update, Delete) capabilities for student records.
- **Attendance Management**: View and export attendance records to CSV.
- **Train Data**: Easily train the facial recognition model with captured images.
- **Modern UI**: A responsive, grid-based layout with a professional aesthetic, using a custom color palette and modern typography (Helvetica).
- **Secure Login**: Authentication system to access the dashboard.
- **MySQL Database Integration**: Robust data storage for student details.

## Technologies Used

- **Python 3.x**
- **Tkinter**: For building the graphical user interface.
- **OpenCV (`cv2`)**: For image processing and face recognition.
- **Pillow (`PIL`)**: For image handling in Tkinter.
- **MySQL**: Database for storing user and student information.
- **NumPy**: For numerical computations during model training.

## Installation

### Prerequisites
- Python 3.7 or higher
- MySQL Server

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/revanthkumar257/smart-class-attendance-system.git
   cd smart-class-attendance-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the Database:**
   Ensure your MySQL server is running. You can run the setup script to initialize the database and tables:
   ```bash
   python setup_db.py
   ```
   *Note: Update the database credentials in `setup_db.py`, `student.py`, `login.py`, `attendance.py`, and `face_recognition.py` if your MySQL configuration differs from the defaults.*

4. **Run the application:**
   ```bash
   python main.py
   ```
   *(Alternatively, run `python login.py` to start from the login screen.)*

## Usage Flow

1. **Login**: Enter your credentials to access the main dashboard.
2. **Student Details**: Add new students and capture their photos using the webcam.
3. **Train Model**: Train the LBPH Face Recognizer with the captured photos.
4. **Take Attendance**: Start the face recognition module to detect faces and mark attendance.
5. **View Attendance**: Check the marked attendance and export the data to a CSV file.

## Repository Details

[GitHub Repository Link](https://github.com/revanthkumar257/smart-class-attendance-system)

## License

This project is licensed under the MIT License.
