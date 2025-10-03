	# Program Name: Assignment3.py (use the name the program is saved as)
	# Course: IT3883/Section W02
	# Student Name: Mason Gilbert
	# Assignment Number: Assignment 3
	# Due Date: 10/3/2025
	# Purpose: This program allows for users to input an number as MPG and will automatically convert it to KM/L. If there is no number, nothing will be displayed.
  # List Specific resources used to complete the assignment. (PyCharm as an IDE), GeeksforGeeks, W3Schools, Python.org, Tutorialspoint, KSU Slideshows
import tkinter as t
conversion = 0.425143707
#This function converses an MPG input to KM/L
def converse(event = None):
    mpg = float(mpg_input.get())
    km = mpg * conversion
    result.config(text=f"{km:.2f} KM/L")
#This creates the GUI window
root = t.Tk()
root.title("MPG to KM/L Converter")
t.Label(root, text="Miles per Gallon(MPG):").grid(row = 0, column = 0, padx = 12, pady = 12)
#This is where the MPG input label is
mpg_input= t.Entry(root, width = 25)
mpg_input.grid(row = 0, column = 0, padx = 12, pady = 12)
mpg_input.bind("<KeyRelease>", converse)
#This is the KM/L output Label
t.Label(root, text = "Kilometers per Liter(KM/L):").grid(row = 1, column = 0, padx = 12, pady = 12)
#This is the results label
result= t.Label(root, text="", fg ="red")
result.grid(row = 1, column = 1, padx = 12, pady = 12)
#This will run the program
root.mainloop()

