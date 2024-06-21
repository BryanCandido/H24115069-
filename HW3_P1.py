#Problem 3_1
n = int(input("Enter the total number of students: "))

students = list(range(1, n+1))

current_student = 0
counter = 0

while len(students) > 1:
    counter += 1

    if counter % 3 == 0:
        students = students[:current_student] + students[current_student+1:]
    else:
        current_student = (current_student + 1) % len(students)

print("The last student remaining is:", students[0])