student_heights = [180,124,165,173,189,169,176]

num_students = 0
total_heights = 0
for student in student_heights:
	total_heights += student
	num_students += 1

average = total_heights / num_students
print(f"The average height is {average}")