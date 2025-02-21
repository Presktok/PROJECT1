import cv2   #OpenCV library for capturing photos using the webcam.
import time   #Used for delays, such as allowing the webcam to warm up.
import tkinter as tk   #Python's standard library for creating GUIs.
from tkinter import messagebox   #Part of tkinter, provides popup messages (e.g., for errors or success notifications).
import threading                #Used to perform background tasks without blocking the GUI.
import pyautogui                #For controlling the mouse cursor.
from PIL import Image, ImageTk  # For handling background images

# Correct credentials
CORRECT_USERNAME = "prince"
CORRECT_PASSWORD = "123"

lock_cursor_flag = False  # Flag to control cursor locking

def authenticate():
    """Authenticate the user."""
    username = username_entry.get()
    password = password_entry.get()

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        unlock_cursor()
        messagebox.showinfo("Access", "Access granted!")
        root.destroy()  # Close the app
    else:
        messagebox.showerror("Access Denied", "Wrong credentials!")
        lock_cursor()  # Freeze the cursor
        capture_photo()  # Take a photo of the unauthorized user

def capture_photo():
    """Capture a photo using the webcam."""
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        unlock_cursor()  # Unlock the cursor if camera access fails
        return

    # ensures the camera stabilizes before capturing the photo.
    time.sleep(2)

    ret, frame = camera.read() #indicates success or failure of the camera operation and the captured photo.
    if ret:
        filename = "unauthorized_access.jpg"
        cv2.imwrite(filename, frame)  # Save the captured photo
    else:
        messagebox.showerror("Error", "Failed to capture photo.")

    camera.release()
    cv2.destroyAllWindows()
    unlock_cursor()  # Unlock the cursor after capturing the photo

def lock_cursor():
    """Freeze the cursor at the center of the screen."""
    global lock_cursor_flag
    lock_cursor_flag = True

    def lock_loop():
        screen_width, screen_height = pyautogui.size() #dimensions of the screen (width and height) in pixels.
        center_x, center_y = screen_width // 2, screen_height // 2

        while lock_cursor_flag:
            pyautogui.moveTo(center_x, center_y)  # Continuously move the cursor to the center

    # Run the locking loop in a separate thread to avoid blocking the main GUI
    threading.Thread(target=lock_loop, daemon=True).start()

def unlock_cursor():
    """Unlock the cursor."""
    global lock_cursor_flag
    lock_cursor_flag = False

# GUI Setup
root = tk.Tk() #Creates the main window
root.title("shield") #Sets the window's title

# Make the window fullscreen
root.attributes("-fullscreen", True)

# Prevent closing the app without authentication
def on_closing():
    messagebox.showwarning("Warning", "You cannot close the app without logging in!")

root.protocol("WM_DELETE_WINDOW", on_closing) #Prevents users from closing the app without logging in.

# Load the background image
background_image_path = r"C:\Users\princ\digital_20security_20padlock_20connected_20to_20numbers.webp"  # Path to the .webp file
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))

# Create a canvas to display the background
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw") #Adds the image to the GUI.

# Create a Frame for the Login Box
login_box = tk.Frame(root, bg="black", bd=5, relief="ridge")  # Box with a border
login_box.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)  # Position at center

# Add Widgets Inside the Login Box
username_label = tk.Label(login_box, text="Username:", font=("Arial", 14), bg="black", fg="white")
username_entry = tk.Entry(login_box, font=("Arial", 12))
password_label = tk.Label(login_box, text="Password:", font=("Arial", 14), bg="black", fg="white") #Displays text like "Username:" and "Password"
password_entry = tk.Entry(login_box, show="*", font=("Arial", 12))
login_button = tk.Button(login_box, text="Login", font=("Arial", 12), command=authenticate)

# Pack Widgets in the Login Box
username_label.pack(pady=5)
username_entry.pack(pady=2, fill="x", padx=5)
password_label.pack(pady=5)
password_entry.pack(pady=2, fill="x", padx=5)
login_button.pack(pady=5)

#Keeps the GUI responsive and running.
root.mainloop()