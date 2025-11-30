import tkinter as tk
import time
import math
from PIL import Image, ImageTk


# Create main window
window = tk.Tk()
window.title("Analog Clock")
window.geometry("400x400")
window.resizable(False, False)

# Load clock face image

clock_face = Image.open("analog.jpg")
clock_face = clock_face.resize((400, 400), Image.LANCZOS)  
clock_img = ImageTk.PhotoImage(clock_face)


# Create canvas
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# Draw clock face
canvas.create_image(200, 200, image=clock_img)
canvas.image = clock_img  

# Draw clock hands
hour_hand = canvas.create_line(200, 200, 200, 10, width=6, fill="black")
minute_hand = canvas.create_line(200, 200, 200, 100, width=4, fill="blue")
second_hand = canvas.create_line(200, 200, 200, 80, width=2, fill="red")

def update_clock():
    now = time.localtime()
    hours = now.tm_hour % 12
    minutes = now.tm_min
    seconds = now.tm_sec

    # Calculate angles
    hour_angle = (hours + minutes / 60) * 30
    minute_angle = (minutes + seconds / 60) * 6
    second_angle = seconds * 6

    # Convert angles to coordinates
    def polar_to_xy(length, angle_deg):
        angle_rad = math.radians(angle_deg - 90)
        x = 200 + length * math.cos(angle_rad)
        y = 200 + length * math.sin(angle_rad)
        return x, y

    hx, hy = polar_to_xy(60, hour_angle)
    mx, my = polar_to_xy(90, minute_angle)
    sx, sy = polar_to_xy(110, second_angle)

    canvas.coords(hour_hand, 200, 200, hx, hy)
    canvas.coords(minute_hand, 200, 200, mx, my)
    canvas.coords(second_hand, 200, 200, sx, sy)

    window.after(1000, update_clock)

update_clock()
window.mainloop()
