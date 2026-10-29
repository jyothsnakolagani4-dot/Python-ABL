# Case Study 3: Student Performance Trend Analysis
# PDF Topic No. 17

subject_count = int(input("Enter number of subjects: "))
exam_count = 3

if subject_count <= 0:
    print("Invalid input: number of subjects must be greater than zero.")
else:
    subjects = []
    marks_list = []

    for i in range(subject_count):
        subject = input("\nEnter subject name: ").strip()

        while subject == "":
            print("Subject name cannot be empty.")
            subject = input("Enter subject name: ").strip()

        marks = []
        valid_subject = True

        for exam in range(1, exam_count + 1):
            mark = float(input("Enter marks for " + subject +
                               " in Exam " + str(exam) + " (0-100): "))

            if mark < 0 or mark > 100:
                print("Invalid marks. Marks must be between 0 and 100.")
                valid_subject = False
                break

            marks.append(mark)

        if not valid_subject:
            print("Please run the program again and enter valid marks.")
            break

        subjects.append(subject)
        marks_list.append(marks)

    if len(subjects) == subject_count:
        total_marks = 0
        total_scores = 0
        weak_subjects = []

        print("\n--- Student Performance Report ---")

        for i in range(subject_count):
            subject = subjects[i]
            marks = marks_list[i]
            average = sum(marks) / exam_count
            change = marks[-1] - marks[0]

            total_marks += sum(marks)
            total_scores += exam_count

            if average >= 75:
                category = "Excellent"
            elif average >= 60:
                category = "Good"
            elif average >= 40:
                category = "Needs Improvement"
            else:
                category = "At Risk"

            if average < 40:
                weak_subjects.append(subject)

            if change > 0:
                trend = "Improved"
            elif change < 0:
                trend = "Declined"
            else:
                trend = "No change"

            print("\nSubject:", subject)
            print("Average marks:", round(average, 2))
            print("Change from Exam 1 to Exam 3:", round(change, 2))
            print("Trend:", trend)
            print("Performance category:", category)

        overall_average = total_marks / total_scores
        print("\nOverall average:", round(overall_average, 2), "%")

        if overall_average >= 75:
            print("Overall classification: Excellent")
        elif overall_average >= 60:
            print("Overall classification: Good")
        elif overall_average >= 40:
            print("Overall classification: Needs Improvement")
        else:
            print("Overall classification: At Risk")

        if weak_subjects:
            print("Subjects needing attention:", ", ".join(weak_subjects))
        else:
            print("No subjects are below the 40% average threshold.")