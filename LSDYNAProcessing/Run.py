# ----- Import libraries -----
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from PIL import Image, ImageTk

# ----- Import functions -----
from EnergyCalculation import all_contact_energy
from NumericalGraphicalOutput import contact_energy_loss, contact_graph

folders = []
directions = ['X']
contacts = [0]
types = ['Force']


def open_folder():
    """
    Opens a dialog to select a folder, then prints the folder path.
    """

    # Delete selected folder from earlier
    folders.clear()

    # Also delete the selected file label
    for index, widget in enumerate(file_frame.winfo_children()):
        # Don't delete the 'selected folder' label
        if index == 0:
            pass
        else:
            widget.destroy()

    folder_selected = filedialog.askdirectory()
    folders.append(folder_selected)

    for folder in folders:
        label = tk.Label(file_frame, text=folder, fg="White", bg="#236D42",
                         wraplength=300, justify='center')
        label.pack()


def process_data():
    """
    Runs the all_contact_energy function to process the data, then prints
    a status reading.
    """

    for folder in folders:
        status = all_contact_energy(fr'{folder}')

        if status == "done":
            messagebox.showinfo("Success!", "Data processing done!")


def plot():
    """
    Plots the force/displacement graph in the graphing window.
    """

    # Clear the existing plot
    for widget in graphing_frame.winfo_children():
        widget.destroy()

    # Create the figure that will contain the plot
    fig = Figure(figsize=(10, 5), dpi=100)

    folder_path = folders[0]
    data_path = os.path.join(folder_path, 'ProcessedData')

    direction = directions[0]
    contact = contacts[0]
    y_type = types[0]

    # Take data from the Processed Data sub-folder
    x, y = contact_graph(contact, fr'{data_path}', direction, y_type)

    # Create a subplot
    plot1 = fig.add_subplot(111)

    # Plotting the graph
    plot1.plot(x, y)
    plot1.set_xlabel(f"Location in {direction} direction [mm]")
    plot1.set_ylabel(f"Force in {direction} direction [kNm]")
    plot1.title.set_text(f"{y_type}/location graph in {direction} direction, "
                         f"contact number {contact}")
    plot1.grid()
    plot1.invert_xaxis()

    # Create Tkinter containing the matplotlib figure
    figure = FigureCanvasTkAgg(fig, master=graphing_frame)
    figure.draw()
    figure.get_tk_widget().pack()

    # Create matplotlib toolbar
    toolbar = NavigationToolbar2Tk(figure,
                                   graphing_frame)
    toolbar.update()
    figure.get_tk_widget().pack()


def energy_calc():
    """
    Calculates the total amount of energy lost for a given contact number.
    """

    folder_path = folders[0]
    data_path = os.path.join(folder_path, 'ProcessedData')
    contact = contacts[0]

    loss = contact_energy_loss(contact, data_path)

    messagebox.showinfo("Energy Loss",
                        f"{loss:.0f} J for contact {contact}")


# ----- tkinter base -----
# Create root for tkinter
root = tk.Tk(className=r" LS-DYNA Postprocessor")

# Create background canvas
canvas = tk.Canvas(root, height=700, width=1000, bg="#263D42")
canvas.pack()

# ----- Frames -----
# Create four frames to contain widgets
logo_frame = tk.Frame(root, bg="white")
logo_frame.place(relwidth=0.23, relheight=0.15, relx=0.02, rely=0.02)

button_frame = tk.Frame(root, bg="white")
button_frame.place(relwidth=0.37, relheight=0.15, relx=0.25, rely=0.02)

file_frame = tk.Frame(root, bg="#236D42")
file_frame.place(relwidth=0.35, relheight=0.15, relx=0.63, rely=0.02)

graphing_frame = tk.Frame(root, bg="white")
graphing_frame.place(relwidth=0.96, relheight=0.79, relx=0.02, rely=0.19)

# Give the file frame a header
header_box = tk.Label(file_frame, text="Selected folder:",
                      bg="#236D42", fg="white")
header_box.pack()

# ----- Buttons -----
# Button to open folder
open_folder_button = tk.Button(button_frame, text="Select Folder",
                               fg="White", bg="#263D42",
                               width=12, justify='left',
                               command=open_folder)
open_folder_button.place(x=30, y=10)

# Button to process data
data_processor_button = tk.Button(button_frame, text="Process Data",
                                  fg="White", bg="#263D42",
                                  width=12, justify='left',
                                  command=process_data)
data_processor_button.place(x=30, y=40)

# Button to calculate energy
energy_button = tk.Button(button_frame, text="Energy Calc",
                          fg="White", bg="#263D42",
                          width=12, justify='left',
                          command=energy_calc)

energy_button.place(x=30, y=70)

# Button to display plot
plot_button = tk.Button(button_frame, text="Plot", padx=10, pady=5,
                        fg="White", bg="#263D42",
                        width=23, justify='left',
                        command=plot)

plot_button.place(x=140, y=50)


# ----- Dropdown menu support functions -----
def direction_select(selected_option):
    directions.clear()
    directions.append(selected_option)


def contact_select(selected_option):
    contacts.clear()
    contacts.append(selected_option)


def type_select(selected_option):
    types.clear()
    types.append(selected_option)


# ----- Dropdown menus -----
# List of direction_options for the dropdown
direction_options = ["X", "Y", "Z"]

# Variable to store the selected option
direction_variable = tk.StringVar(button_frame)
direction_variable.set(direction_options[0])  # Set the default option

# Create the dropdown menu
direction_dropdown = tk.OptionMenu(button_frame, direction_variable,
                                   *direction_options, command=direction_select)
direction_dropdown.place(x=140, y=10)

# List of direction_options for the dropdown
contact_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Variable to store the selected option
contact_variable = tk.StringVar(button_frame)
contact_variable.set(contact_options[0])  # Set the default option

# Create the dropdown menu
contact_dropdown = tk.OptionMenu(button_frame, contact_variable,
                                 *contact_options, command=contact_select)
contact_dropdown.place(x=200, y=10)

image = Image.open('hsg_logo.png')
image = ImageTk.PhotoImage(image)

# List of direction_options for the dropdown
type_options = ["Force", "Energy"]

# Variable to store the selected option
type_variable = tk.StringVar(button_frame)
type_variable.set(type_options[0])  # Set the default option

# Create the dropdown menu
type_dropdown = tk.OptionMenu(button_frame, type_variable,
                              *type_options, command=type_select)
type_dropdown.place(x=260, y=10)

# Create a label to display the image
image_label = tk.Label(logo_frame, image=image)
image_label.pack()

# ----- tkinter execute ----
root.mainloop()
