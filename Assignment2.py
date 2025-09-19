	# Program Name: Assignment2.py (use the name the program is saved as)
	# Course: IT3883/Section W02
	# Student Name: Mason Gilbert
	# Assignment Number: Assignment 2
	# Due Date: 09/19/2025
	# Purpose: What does the program do (in a few sentences)? This program uses 9 student's grades and calculates the final average for each student. It will print their name and final average in descending order by grade.
	# List Specific resources used to complete the assignment. (PyCharm as an IDE), GeeksforGeeks, W3Schools, Python.org
grade_file = "Assignment2input.txt"
students = [] #List for students

with open(grade_file, 'r') as files: #This will allow the file in read mode
    for line in files:
        sections = line.strip().split()
        if len(sections) == 7:
			#Variables
            name = sections[0]
            score = list(map(float, sections[1:]))
            average = sum(score)/ len(score)
            students.append((name,average))
students.sort(key= lambda x: x[1], reverse=True) #This sorts by average in descending order
for name, average in students:
    print(f"{name} {average: .2f}") #This prints the results
