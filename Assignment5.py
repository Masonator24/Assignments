import sqlite3

file_input = "Assignment5input.txt"
databasename = "Temperatures.db"
conn = sqlite3.connect(databasename)
cursor = conn.cursor()
#This will create the table
cursor.execute("""CREATE TABLE IF NOT EXISTS Temperature ( ID INTEGER PRIMARY KEY,
Days TEXT,
 Temp_Value REAL);""")
#This will open the file and read each input line
with open(file_input) as file:
    for line in file:
        extra_lines = line.strip().split()
        if len(extra_lines) != 2:
            repr(line)
            continue
        day, temp = extra_lines
        #This will insert the data into the table
        cursor.execute("INSERT INTO Temperature (Days, Temp_Value) VALUES (?, ?)", (day, float(temp)))
conn.commit()
#This will calculate the average for Sunday and Thursday and print out the results
for day in ("Sunday", "Thursday"):
    cursor.execute("SELECT AVG(Temp_Value) FROM Temperature WHERE Days = ?", (day,))
    average = cursor.fetchone()[0]
    print(f"Average of {day}: {round(average, 2)}")
conn.close() # This will close out the connection
