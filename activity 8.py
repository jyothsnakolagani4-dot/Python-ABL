# Case Study 8: Student Marks Matrix Analysis
# Topic 42 - Uses nested lists, loops, conditions, and arithmetic.

print("=" * 58)
print("          STUDENT MARKS MATRIX ANALYSIS")
print("=" * 58)

while True:
    try:
        student_count = int(input("Enter number of students: "))
        if student_count > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

while True:
    try:
        subject_count = int(input("Enter number of subjects: "))
        if subject_count > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

subject_names = []
for j in range(subject_count):
    subject = input(f"Enter name of subject {j + 1}: ").strip()
    while subject == "":
        print("Subject name cannot be empty.")
        subject = input(f"Enter name of subject {j + 1}: ").strip()
    subject_names.append(subject)

student_names = []
marks_matrix = []

for i in range(student_count):
    name = input(f"\nEnter name of student {i + 1}: ").strip()
    while name == "":
        print("Student name cannot be empty.")
        name = input(f"Enter name of student {i + 1}: ").strip()
    student_names.append(name)

    marks_row = []
    for j in range(subject_count):
        while True:
            try:
                mark = float(input(f"Enter {subject_names[j]} marks for {name} (0-100): "))
                if 0 <= mark <= 100:
                    marks_row.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a numeric mark.")
    marks_matrix.append(marks_row)

# Row-wise statistics: each student's total and average.
student_totals = []
student_averages = []

for row in marks_matrix:
    total = sum(row)
    average = total / subject_count
    student_totals.append(total)
    student_averages.append(average)

# Column-wise statistics: average for each subject.
subject_totals = []
subject_averages = []

for j in range(subject_count):
    total = 0
    for i in range(student_count):
        total += marks_matrix[i][j]
    subject_totals.append(total)
    subject_averages.append(total / student_count)

highest_average = max(student_averages)
top_students = []
for i in range(student_count):
    if student_averages[i] == highest_average:
        top_students.append(student_names[i])

LOW_AVERAGE_LIMIT = 65.0

print("\n" + "=" * 58)
print("STUDENT-WISE RESULTS")
print("=" * 58)
print(f"{'Student':<18}{'Total':>10}{'Average':>12}")
print("-" * 40)
for i in range(student_count):
    print(f"{student_names[i]:<18}{student_totals[i]:>10.2f}{student_averages[i]:>12.2f}")

print("\nSUBJECT-WISE RESULTS")
print("=" * 58)
print(f"{'Subject':<18}{'Total':>10}{'Average':>12}")
print("-" * 40)
for j in range(subject_count):
    print(f"{subject_names[j]:<18}{subject_totals[j]:>10.2f}{subject_averages[j]:>12.2f}")

print("\nTOP PERFORMER(S)")
print(", ".join(top_students))
print(f"Highest student average: {highest_average:.2f}%")

print(f"\nSUBJECTS WITH AVERAGE BELOW {LOW_AVERAGE_LIMIT:.0f}%")
low_subject_found = False
for j in range(subject_count):
    if subject_averages[j] < LOW_AVERAGE_LIMIT:
        print(f"- {subject_names[j]}: {subject_averages[j]:.2f}%")
        low_subject_found = True
if not low_subject_found:
    print("None")

print("\nAnalysis complete.")