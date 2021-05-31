# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score,
# a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	    A
# 80-89	    B
# 70-79	    C
# 60-69	    D
# 0-59	    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: ")) # added int conversion
exam_three = int(input("Input exam grade three: ")) # changed str to int, changed var name to exam_three

grades = [exam_one, exam_two, exam_three] # added commas to separate variables
sum = 0
for grade in grades: # changed list that loop was referring to to 'grades'
    sum = sum + grade # made indentation consistent with rest of code

avg = round(sum/len(grades), 2) # changed list variable to 'grades', rounded the value to 2 d.p.

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # added colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # added double quotation mark
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F" # changed to else

x = 0 # incrementor for exam_number
for grade in grades:
    exam_number = ['one', 'two', 'three'] # list for output that links each exam to their respective score
    print(f"Exam {exam_number[x]}: {str(grade)}") # formatted string to make more readable and concise in both code and output
    x += 1 # increments x by 1 per loop

# removed redundant print statements from loop function to make the output more readable and useful

print("\nAverage: " + str(avg)) # added line separator for readability in output
print("Grade: " + letter_grade + "\n") # added line separator for readability in output

if letter_grade == "F": # changed letter-grade to letter_grade, changed 'is' to '=='
    print("Student is failing.") # enclosed string in brackets
else:
    print("Student is passing.")  # enclosed string in brackets