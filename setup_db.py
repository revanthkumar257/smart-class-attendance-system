import mysql.connector

def setup_database():
    try:
        # Connect to MySQL server without specifying database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor = conn.cursor()

        # Create Database
        cursor.execute("CREATE DATABASE IF NOT EXISTS face_recognition")
        print("Database 'face_recognition' created or already exists.")

        # Switch to the new database
        cursor.execute("USE face_recognition")

        # Create Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                phone VARCHAR(20)
            )
        ''')
        print("Table 'users' ready.")

        # Create Student table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                dep VARCHAR(50),
                course VARCHAR(50),
                year VARCHAR(10),
                semester VARCHAR(10),
                student_id VARCHAR(50) PRIMARY KEY,
                student_Name VARCHAR(100),
                phone_No VARCHAR(20),
                Email_ID VARCHAR(100),
                gender VARCHAR(20),
                Takephotosample VARCHAR(20)
            )
        ''')
        print("Table 'student' ready.")

        # Create Attendance table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                roll VARCHAR(50) PRIMARY KEY,
                name VARCHAR(100),
                dept VARCHAR(50),
                time VARCHAR(50),
                date VARCHAR(50),
                status VARCHAR(50)
            )
        ''')
        print("Table 'attendance' ready.")

        conn.commit()
        conn.close()
        print("Database setup completed successfully.")

    except Exception as e:
        print(f"Error during database setup: {e}")

if __name__ == "__main__":
    setup_database()
