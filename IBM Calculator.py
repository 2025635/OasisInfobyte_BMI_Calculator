import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        
        bmi_category = classify_bmi(bmi)
        
        bmi_label.config(text="Your BMI: {:.2f}".format(bmi), fg=get_bmi_color(bmi))
        bmi_category_label.config(text="Category: {}".format(bmi_category), fg=get_bmi_color(bmi))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi:
        return "Overweight"

def get_bmi_color(bmi):
    if bmi < 18.5:
        return "blue"  # Underweight
    elif 18.5 <= bmi < 25:
        return "green"  # Normal
    elif 25 <= bmi:
        return "orange"  # Overweight

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.configure(background="black")  # Setting background color of the root window

# Create labels and entry fields for weight and height
weight_label = tk.Label(root, text="Enter your weight (in kg):", fg="blue", font=("Helvetica", 16, "bold"))
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root, font=("Helvetica", 16, "bold"))
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Enter your height (in m):", fg="blue", font=("Helvetica", 16, "bold"))
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root, font=("Helvetica", 16, "bold"))
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, fg="white", bg="blue", font=("Helvetica", 16, "bold"))
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create labels to display the BMI result and category
bmi_label = tk.Label(root, text="", fg="black", font=("Helvetica", 20, "bold"))
bmi_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

bmi_category_label = tk.Label(root, text="", fg="black", font=("Helvetica", 16, "bold"))
bmi_category_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
