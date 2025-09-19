	# Program Name: Assignment2.py (use the name the program is saved as)
	# Course: IT3883/Section W02
	# Student Name: Mason Gilbert
	# Assignment Number: Assignment 2
	# Due Date: 09/19/2025
	# Purpose: What does the program do (in a few sentences)? This program uses 9 student's grades and calculates the final average for each student. It will print their name and final average in descending order by grade.
	# List Specific resources used to complete the assignment. (PyCharm as an IDE), GeeksforGeeks, W3Schools
grade_file = "Assignment2input.txt"
students = []

with open(grade_file, 'r') as files:
    for line in files:
        sections = line.strip().split()
        if len(sections) == 7:
            name = sections[0]
            score = list(map(float, sections[1:]))
            average = sum(score)/ len(score)
            students.append((name,average))
students.sort(key= lambda x: x[1], reverse=True)
for name, average in students:
    print(f"{name} {average: .2f}")
