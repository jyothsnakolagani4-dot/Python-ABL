"""
Case Study 7: String-Based Examination Answer Evaluation
Compare student answer strings with an answer key, score responses,
apply negative marking, and display a result summary.
"""

print("STRING-BASED EXAMINATION ANSWER EVALUATION")
print("------------------------------------------")

while True:
    try:
        question_count = int(input("Enter number of questions: "))
        if question_count > 0:
            break
        print("Enter a number greater than zero.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

answer_key = []
for number in range(1, question_count + 1):
    while True:
        answer = input("Enter correct answer for question " + str(number) +
                       " (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            answer_key.append(answer)
            break
        print("Invalid answer. Enter A, B, C, or D.")

student_count = 0
while True:
    try:
        student_count = int(input("Enter number of students: "))
        if student_count > 0:
            break
        print("Enter a number greater than zero.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

# Scoring assumptions: +1 for correct, -0.25 for incorrect, 0 for unanswered.
CORRECT_MARKS = 1
NEGATIVE_MARKS = 0.25

for student in range(1, student_count + 1):
    print("\nStudent", student)
    student_name = input("Enter student name: ").strip()
    correct = 0
    incorrect = 0
    unanswered = 0

    for question in range(1, question_count + 1):
        response = input("Answer Q" + str(question) + " (A/B/C/D or Enter to skip): ")
        response = response.strip().upper()

        if response == "":
            unanswered += 1
        elif response not in ["A", "B", "C", "D"]:
            print("Invalid option. This response is counted as unanswered.")
            unanswered += 1
        elif response == answer_key[question - 1]:
            correct += 1
        else:
            incorrect += 1

    score = correct * CORRECT_MARKS - incorrect * NEGATIVE_MARKS
    maximum_score = question_count * CORRECT_MARKS
    percentage = (score / maximum_score) * 100

    print("\nResult for", student_name)
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Unanswered questions:", unanswered)
    print("Final score:", round(score, 2), "out of", maximum_score)
    print("Score percentage:", round(percentage, 2), "%")

print("\nEvaluation completed.")