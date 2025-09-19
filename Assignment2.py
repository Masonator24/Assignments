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
