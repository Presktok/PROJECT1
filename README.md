# ACCESS SHIELD
    # ACCESS SHIELD
    Project Title: Webcam Security Authentication System
    Overview
This Python application provides a security authentication system using a graphical user interface (GUI).

It captures a photo of unauthorized users and locks the mouse cursor if incorrect credentials are entered.

The application uses the OpenCV library for webcam access, tkinter for the GUI, and pyautogui for cursor control.

    Key Features
•	User authentication with a username and password.

•	Webcam photo capture of unauthorized access attempts.

•	Cursor locking mechanism to prevent user interaction.

•	Fullscreen GUI with a custom background image.

    Libraries Used
•	OpenCV (cv2): For capturing images from the webcam.

•	tkinter: For creating the GUI.

•	threading: To run background tasks without blocking the GUI.

•	pyautogui: For controlling the mouse cursor.

•	PIL (Pillow): For handling and displaying images.

    Code Breakdown
    Constants
•	CORRECT_USERNAME and CORRECT_PASSWORD: Store the correct login credentials.

•	lock_cursor_flag: A flag to control the cursor locking mechanism.

     Functions
    authenticate()
Retrieves the username and password from the input fields.

Checks if the credentials match the correct ones.

If correct, it unlocks the cursor and closes the application.

If incorrect, it locks the cursor and captures a photo of the user.

    capture_photo()
Initializes the webcam and captures a photo after a brief delay.

Saves the captured photo as "unauthorized_access.jpg".

Unlocks the cursor after capturing the photo.

    lock_cursor()
Locks the cursor at the center of the screen.

Runs a loop in a separate thread to continuously move the cursor to the center while the flag is set.

     unlock_cursor()
Unlocks the cursor by setting the flag to false.

    GUI Setup
Creates a fullscreen window using tkinter.

Prevents the application from being closed without authentication.

Loads a background image for the GUI.

Creates a login box with fields for username and password, and a login button.

    Main Loop
The application runs in a loop, keeping the GUI responsive until the user interacts with it.

    Usage
Run the script using Python.

Enter the username and password to gain access.

If incorrect credentials are entered, the cursor will be locked, and a photo will be taken.

    Installation
To run this application, ensure you have the following libraries installed:

bash

     Run
Copy code

pip install opencv-python

pip install pyautogui

pip install pillow

    License
This project is licensed under the MIT License - see the LICENSE file for details
