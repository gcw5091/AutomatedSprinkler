import tkinter as tk
 
class LawnGUI:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.geometry("450x450")
        self.root.title("My Lawn")
        self.root.resizable(width=False, height=False)
 
        # Define colors and variables
        self.lawnColor = "#15B01A"
        self.highlightColor = "palegreen"
        self.highlighted_buttons = []
 
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="lightgrey")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
 
        # Title of GUI
        label = tk.Label(self.main_frame, text="My Lawn", font=("Arial", 15), bg="lightgrey")
        label.grid(row=0, column=0, columnspan=3, pady=10)
 
        # Create buttons in a 3x3 grid
        self.create_buttons()
 
        # Add Submit Button
        submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_coordinates)
        submit_button.grid(row=4, column=0, columnspan=3, pady=10)  # Place below the grid
 
        # Label to show selected coordinates
        self.coordinates_label = tk.Label(self.main_frame, text="Coordinates: ", font=("Arial", 10, "bold"), bg="lightgrey")
        self.coordinates_label.grid(row=5, column=0, columnspan=3, pady=10)  # Place below the submit button
 
    def create_buttons(self):
        """Creates a 3x3 grid of buttons for the lawn."""
        self.buttons = []
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.main_frame, width=10, height=5, background=self.lawnColor, text=row * 3 + col + 1)
                button.grid(row=row + 1, column=col, padx=2, pady=2)
                button.bind("<Button-1>", self.toggle_highlight)
                self.buttons.append(button)
 
    def toggle_highlight(self, event):
        """Toggle the button highlight state and update coordinates display."""
        button = event.widget
        if button['bg'] == self.lawnColor:
            button.config(bg=self.highlightColor)
            self.highlighted_buttons.append(int(button['text']))
        else:
            button.config(bg=self.lawnColor)
            self.highlighted_buttons.remove(int(button['text']))
 
        # Update the displayed coordinates after each selection
        self.update_coordinates_label()
 
    def update_coordinates_label(self):
        """Update the coordinates label to reflect current highlighted buttons."""
        coordinates = []
        for button_num in self.highlighted_buttons:
            x = (button_num - 1) % 3
            y = (button_num - 1) // 3
            coordinates.append((x, y))
        # Update the label text
        self.coordinates_label.config(text=f"Coordinates: {coordinates}")
 
    def submit_coordinates(self):
        """Gather selected coordinates, store them, and close the GUI."""
        coordinates = []
        for button_num in self.highlighted_buttons:
            x = (button_num - 1) % 3  # Column index (0 to 2)
            y = (button_num - 1) // 3  # Row index (0 to 2)
            coordinates.append((x, y))
        # Store the coordinates for access by MainController
        self.selected_coordinates = coordinates
        # Close the GUI window
        self.root.quit()
 
    def run(self):
        """Start the GUI."""
        self.root.mainloop()
