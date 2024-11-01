import tkinter as tk

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

# Function to handle submission
def submit_coordinates(event):
    if highlighted_buttons:
        coordinates = []
        for button_num in highlighted_buttons:
            # Mapping button number to (x, y) coordinates in meters
            x = (button_num - 1) % 3  # Column index (0 to 2)
            y = (button_num - 1) // 3  # Row index (0 to 2)

            # Convert to meters (each button represents a 1m x 1m section)
            coordinates.append((x, y))

        # Simulate sending coordinates to the main controller
        print("Coordinates sent to main controller:", coordinates)
        coordinates_label.config(text=f"Coordinates: {coordinates}")
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
