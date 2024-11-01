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

# Create main frame
main_frame = tk.Frame(root, bg=bgColor)
main_frame.pack(fill=tk.BOTH, expand=True)

# Title
label = tk.Label(main_frame, text="My Lawn", font=("Arial", 15), bg=bgColor)
label.grid(row=0, column=0, columnspan=3, pady=10)

# Function to toggle button highlight
def toggle_highlight(event):
    button = event.widget  # Get the button that was pressed
    if button['bg'] == lawnColor:
        button.config(bg=highlightColor)
    else:
        button.config(bg=lawnColor)

def toggle_submit(event):
    button = event.widget  # Get the button that was pressed
    if button['bg'] == 'gray':
        button.config(bg='lightgrey')
    else:
        button.config(bg='gray')

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
submit_button.bind("<Button-1>", toggle_submit)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)  # Placed below the grid of buttons

# Create a label to display "Coordinates:"
coordinates_label = tk.Label(main_frame, text="Coordinates: ", font=("Arial", 10, "bold"), bg=bgColor, anchor='w')  # Align to the left
coordinates_label.grid(row=5, column=0, columnspan=1, pady=10)  # Placed directly below the submit button

# Submit Coordinates to Master Controller



# Run the application
root.mainloop()

