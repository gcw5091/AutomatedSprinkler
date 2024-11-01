import tkinter as tk
import numpy as np

# Create main window
root = tk.Tk()
root.geometry("450x450")  # Adjust size as needed
root.title("My Lawn")
root.resizable(width=False, height=False)

# Define variables
lawnColor = "#15B01A"
highlightColor = "palegreen"
bgColor = "lightgrey"
highlighted_buttons = []  # Stores highlighted button coordinates

# Create main frame
main_frame = tk.Frame(root, bg=bgColor)
main_frame.pack(fill=tk.BOTH, expand=True)

# Title of GUI
label = tk.Label(main_frame, text="My Lawn", font=("Arial", 15), bg=bgColor)
label.grid(row=0, column=0, columnspan=3, pady=10)

# Function to toggle button highlight
def toggle_highlight(event):
    button = event.widget  # Get button when pressed
    if button['bg'] == lawnColor:
        button.config(bg=highlightColor)
        # Add button coordinates to the list
        highlighted_buttons.append(int(button['text']))
    else:
        button.config(bg=lawnColor)
        # Remove button coordinates from list
        highlighted_buttons.remove(int(button['text']))

def toggle_submit(event):
    button = event.widget  # Get button that was pressed
    if button['bg'] == 'gray':
        button.config(bg='lightgrey')
    else:
        button.config(bg='gray')

# Function to calculate angles
def calc_angles(x, y, h):
    yaw_ang = np.arctan2(y, x) * 360 / (2 * np.pi)  
    pitch_ang = 0  # Default pitch angle
    return yaw_ang, pitch_ang

# Function to handle submission
def submit_coordinates(event):
    if highlighted_buttons:
        for button_num in highlighted_buttons:
            # Mapping based on button number (placeholder).
            # Assume button number corresponds to x,y coordinates
            x = (button_num - 1) % 3  # Column index
            y = (button_num - 1) // 3  # Row index

            # height (can be modified as needed)
            h = 1.0  
            yaw, pitch = calc_angles(x, y, h)
            coordinates_label.config(text=f"Coordinates: ({x}, {y}), Yaw: {yaw:.2f}, Pitch: {pitch:.2f}")
    else:
        coordinates_label.config(text="Coordinates: No buttons selected")

# Create buttons in a 3x3 grid
buttons = []
for row in range(3):
    for col in range(3):
        button = tk.Button(main_frame, width=10, height=5, background=lawnColor,
                           text=row * 3 + col + 1)
        button.grid(row=row + 1, column=col, padx=2, pady=2)  # Adjusted row index
        button.bind("<Button-1>", toggle_highlight)  # Bind left mouse button click
        buttons.append(button)

# Create Submit Button
submit_button = tk.Button(main_frame, width=10, height=2, background='gray', text='Submit')
submit_button.bind("<Button-1>", submit_coordinates)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)  # Placed below grid of buttons

# Create a label to display "Coordinates:"
coordinates_label = tk.Label(main_frame, text="Coordinates: ", font=("Arial", 10, "bold"), bg=bgColor, anchor='w')  # Align to the left
coordinates_label.grid(row=5, column=0, columnspan=3, pady=10)  # Placed below submit button

# Run the application
root.mainloop()

