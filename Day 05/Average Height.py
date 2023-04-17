student_heights = input("Input a list of student heights \n").split(", ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_heights = 0
for height in student_heights:
    total_heights += height

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average_height = total_heights / number_of_students
print(round(average_height))
