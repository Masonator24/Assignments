o	# Program Name: Assignment1.py (use the name the program is saved as)
o	# Course: IT3883/Section W02
o	# Student Name: Mason Gilbert
o	# Assignment Number: Assignment 1
o	# Due Date: 09/05/ 2025
o	# Purpose: What does the program do (in a few sentences)?
o	# List Specific resources used to complete the assignment.
input_buff = ""
print("Please choose one of the following 4 choices: ")
while True:
    print("1) Append Data to the input buffer")
    print("2) Clear the input buffer")
    print("3) Display the input buffer")
    print("4) Exit the program")
    choice = input()
    match choice:
        case "1":
            data = input("Enter your data to be appended: ")
            input_buff += data
        case "2":
            input_buff = ""
            print("Data has been cleared.")
        case "3":
            if input_buff == "":
                print("Input Buffer Empty.")
            else:
                print(f"Input Buffer: {input_buff}")
        case "4":
            print("Exiting terminal...")
            break
