import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
import cv2
import platform

# Function to get location
def get_location():
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode("Your Location")
        return location.address
    except Exception as e:
        return str(e)

# Function to access camera
def access_camera():
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Camera", frame)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()
                cap.release()
                return "Camera accessed successfully"
            else:
                return "Failed to capture frame"
        else:
            return "Failed to open camera"
    except Exception as e:
        return str(e)

# Function to get device particulars
def get_device_particulars():
    try:
        system = platform.system()
        machine = platform.machine()
        processor = platform.processor()
        return f"System: {system}\nMachine: {machine}\nProcessor: {processor}"
    except Exception as e:
        return str(e)

# GUI setup
root = tk.Tk()
root.title("Device Information")

location_label = tk.Label(root, text="Location:")
location_label.pack()

location_entry = tk.Entry(root)
location_entry.pack()

camera_button = tk.Button(root, text="Access Camera", command=lambda: messagebox.showinfo("Camera Access", access_camera()))
camera_button.pack()

device_info_button = tk.Button(root, text="Get Device Particulars", command=lambda: messagebox.showinfo("Device Particulars", get_device_particulars()))
device_info_button.pack()

root.mainloop()
