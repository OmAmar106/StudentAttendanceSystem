# Student Attendance System

This Student Attendance System is implemented entirely in Python. It provides two versions: one that uses file handling for a standalone database system and another that integrates with MySQL as the database software, leveraging external modules.

## Features

- **Multi-Interface**: Users can log in as Admin, Student, or Teacher.
- **Admin Functions**: Admins have the ability to view and update details for both teachers and students. The admin password is set to `#pas123` by default and can be updated only by changing the code.
- **Student Functions**: Students can scan QR codes, read messages sent by teachers, change their passwords, and more.
- **Teacher Functions**: Teachers can generate QR codes for class attendance, send messages to students, change their passwords, and more.

## System Components

### 1. File Handling Version
- **Database**: Uses file-based storage for data management.
- **Portability**: The database can be copied and used on different systems.

### 2. MySQL Version
- **Database**: Utilizes MySQL for data storage and management.
- **External Modules**: Requires additional modules for MySQL integration.

## User Interfaces

### Admin
- **Login**: Admin login credentials are hard-coded as `#pas123`. Update the password by modifying the code.
- **Functions**: View and update details of teachers and students.

### Student
- **Functions**: 
  - Open QR Code Scanner.
  - Read messages sent by teachers.
  - Change password.
  - Additional functions as implemented.

### Teacher
- **Functions**: 
  - Create QR Codes by providing a link.
  - Send messages to students of a particular class.
  - Change password.
  - Additional functions as implemented.

## Installation and Setup

1. **File Handling Version**:
   - Ensure Python is installed.
   - Run the Python script to start the system.

2. **MySQL Version**:
   - Install MySQL and required Python modules (`mysql-connector-python` or similar).
   - Set up the database schema and credentials as per the script instructions.
   - Run the Python script to start the system.

## Example Usage

1. **Admin Login**:
   - Start the program.
   - Log in using the password `#pas123`.
   - Access admin functionalities to manage teachers and students.

2. **Student Actions**:
   - Log in with credentials created by the admin.
   - Scan QR codes or read messages from teachers.

3. **Teacher Actions**:
   - Log in with credentials created by the admin.
   - Generate QR codes or send messages to students.

## Contributing

Contributions to improve the system are welcome. Please submit issues or pull requests if you have suggestions for enhancements or additional features.
